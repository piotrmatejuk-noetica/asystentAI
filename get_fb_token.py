#!/usr/bin/env python3
"""
Pobiera Page Access Token dla SACRUM (Facebook + Instagram).
Uruchom: python3 get_fb_token.py
Potem otwórz URL który wypisze i kliknij Authorize.
Token zostanie zapisany do .env automatycznie.
"""
import http.server
import urllib.parse
import urllib.request
import json
import os
import sys
import webbrowser
from pathlib import Path

APP_ID = "937795249248975"
REDIRECT_URI = "http://localhost:8765/callback"
SCOPES = "pages_manage_posts,pages_show_list,pages_read_engagement,instagram_basic,instagram_content_publish"

VAULT = Path(__file__).parent
ENV_FILE = VAULT / ".env"

captured_token = {}


def load_env():
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text().splitlines():
            if "=" in line and not line.startswith("#"):
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())


def save_env(key, value):
    content = ENV_FILE.read_text() if ENV_FILE.exists() else ""
    lines = content.splitlines()
    updated = False
    for i, line in enumerate(lines):
        if line.startswith(f"{key}="):
            lines[i] = f"{key}={value}"
            updated = True
            break
    if not updated:
        lines.append(f"{key}={value}")
    ENV_FILE.write_text("\n".join(lines) + "\n")
    print(f"  ✅ {key} zapisany do .env")


def exchange_short_for_long(short_token, app_secret):
    url = (
        f"https://graph.facebook.com/v20.0/oauth/access_token"
        f"?grant_type=fb_exchange_token"
        f"&client_id={APP_ID}"
        f"&client_secret={app_secret}"
        f"&fb_exchange_token={short_token}"
    )
    with urllib.request.urlopen(url) as r:
        return json.loads(r.read())["access_token"]


def get_page_token(long_token, app_secret):
    url = f"https://graph.facebook.com/v20.0/me/accounts?access_token={long_token}"
    with urllib.request.urlopen(url) as r:
        data = json.loads(r.read())

    pages = data.get("data", [])
    if not pages:
        print("Nie znaleziono stron FB na tym koncie.")
        sys.exit(1)

    print("\nZnalezione strony:")
    for i, p in enumerate(pages):
        print(f"  [{i}] {p['name']} (ID: {p['id']})")

    if len(pages) == 1:
        idx = 0
    else:
        idx = int(input("Wybierz numer strony SACRUM: "))

    page = pages[idx]
    return page["id"], page["name"], page["access_token"]


def get_ig_account(page_id, page_token):
    url = f"https://graph.facebook.com/v20.0/{page_id}?fields=instagram_business_account&access_token={page_token}"
    with urllib.request.urlopen(url) as r:
        data = json.loads(r.read())
    ig = data.get("instagram_business_account", {})
    return ig.get("id")


class CallbackHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)

        if "code" in params:
            code = params["code"][0]
            app_secret = os.environ.get("FB_APP_SECRET", "")

            # zamień code na short-lived token
            token_url = (
                f"https://graph.facebook.com/v20.0/oauth/access_token"
                f"?client_id={APP_ID}"
                f"&redirect_uri={urllib.parse.quote(REDIRECT_URI)}"
                f"&client_secret={app_secret}"
                f"&code={code}"
            )
            with urllib.request.urlopen(token_url) as r:
                short_token = json.loads(r.read())["access_token"]

            print("\n[1/4] Short-lived token ✅")

            # zamień na long-lived (60 dni)
            long_token = exchange_short_for_long(short_token, app_secret)
            print("[2/4] Long-lived token ✅")

            # pobierz page token
            page_id, page_name, page_token = get_page_token(long_token, app_secret)
            print(f"[3/4] Page token dla '{page_name}' ✅")

            # pobierz IG account
            ig_id = get_ig_account(page_id, page_token)
            print(f"[4/4] Instagram Business Account ID: {ig_id or 'nie znaleziono'}")

            # zapisz wszystko
            save_env("FB_PAGE_ID", page_id)
            save_env("FB_PAGE_TOKEN", page_token)
            if ig_id:
                save_env("IG_ACCOUNT_ID", ig_id)

            captured_token["done"] = True

            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write("<h2>Gotowe! Token zapisany. Wróc do terminala.</h2>".encode("utf-8"))
        else:
            self.send_response(400)
            self.end_headers()
            self.wfile.write("Blad: brak kodu autoryzacji.".encode("utf-8"))

    def log_message(self, format, *args):
        pass


def main():
    load_env()

    app_secret = os.environ.get("FB_APP_SECRET")
    if not app_secret and len(sys.argv) > 1:
        app_secret = sys.argv[1].strip()
        save_env("FB_APP_SECRET", app_secret)
        os.environ["FB_APP_SECRET"] = app_secret
    if not app_secret:
        print("Podaj App Secret jako argument: python3 get_fb_token.py <APP_SECRET>")
        print("Znajdziesz go na: developers.facebook.com/apps/937795249248975/settings/basic/")
        sys.exit(1)

    auth_url = (
        f"https://www.facebook.com/v20.0/dialog/oauth"
        f"?client_id={APP_ID}"
        f"&redirect_uri={urllib.parse.quote(REDIRECT_URI)}"
        f"&scope={SCOPES}"
        f"&response_type=code"
    )

    print(f"\nOtwieranie przeglądarki...")
    print(f"Jeśli nie otworzy się samo, wejdź na:\n{auth_url}\n")
    webbrowser.open(auth_url)

    server = http.server.HTTPServer(("localhost", 8765), CallbackHandler)
    print("Czekam na autoryzację (kliknij 'Kontynuuj' w przeglądarce)...")
    while not captured_token.get("done"):
        server.handle_request()

    print("\n✅ Wszystko gotowe. Tokeny zapisane w .env")


if __name__ == "__main__":
    main()
