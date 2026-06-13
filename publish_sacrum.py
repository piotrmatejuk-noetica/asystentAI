#!/usr/bin/env python3
"""
Publikuje post na Facebook SACRUM (+ Instagram jeśli skonfigurowane).

Użycie:
  python3 publish_sacrum.py "Twój tekst posta"
  python3 publish_sacrum.py "Twój tekst" --img https://url-do-zdjecia.jpg
  python3 publish_sacrum.py "Twój tekst" --fb-only
  python3 publish_sacrum.py "Twój tekst" --ig-only
"""
import sys
import os
import urllib.request
import urllib.parse
import json
import argparse
from pathlib import Path

VAULT = Path(__file__).parent
GRAPH = "https://graph.facebook.com/v20.0"


def load_env():
    env_file = VAULT / ".env"
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            if "=" in line and not line.startswith("#"):
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())


def api_post(url, payload):
    data = json.dumps(payload).encode()
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read())


def publish_fb(page_id, page_token, text, img_url=None):
    if img_url:
        payload = {"url": img_url, "caption": text, "access_token": page_token}
        result = api_post(f"{GRAPH}/{page_id}/photos", payload)
    else:
        payload = {"message": text, "access_token": page_token}
        result = api_post(f"{GRAPH}/{page_id}/feed", payload)
    return result.get("id", "")


def publish_ig(ig_user_id, page_token, text, img_url):
    if not img_url:
        print("[IG] Pominięto — Instagram wymaga zdjęcia")
        return ""
    container = api_post(f"{GRAPH}/{ig_user_id}/media", {
        "image_url": img_url,
        "caption": text,
        "access_token": page_token,
    })
    container_id = container["id"]
    result = api_post(f"{GRAPH}/{ig_user_id}/media_publish", {
        "creation_id": container_id,
        "access_token": page_token,
    })
    return result.get("id", "")


def main():
    load_env()

    parser = argparse.ArgumentParser(description="Publikuj post SACRUM")
    parser.add_argument("text", help="Treść posta")
    parser.add_argument("--img", help="URL zdjęcia (wymagany dla Instagram)", default="")
    parser.add_argument("--fb-only", action="store_true")
    parser.add_argument("--ig-only", action="store_true")
    args = parser.parse_args()

    page_id = os.environ.get("FB_PAGE_ID_SACRUM", "")
    page_token = os.environ.get("FB_PAGE_TOKEN_SACRUM", "")
    ig_id = os.environ.get("IG_ACCOUNT_ID_SACRUM", "")

    if not page_id or not page_token:
        print("Brak FB_PAGE_ID_SACRUM lub FB_PAGE_TOKEN_SACRUM w .env")
        sys.exit(1)

    results = {}

    if not args.ig_only:
        try:
            post_id = publish_fb(page_id, page_token, args.text, args.img or None)
            results["facebook"] = f"https://www.facebook.com/{post_id}"
            print(f"[FB] Opublikowano: {results['facebook']}")
        except Exception as e:
            print(f"[FB] Blad: {e}")
            results["facebook"] = f"BLAD: {e}"

    if not args.fb_only and ig_id:
        try:
            ig_post_id = publish_ig(ig_id, page_token, args.text, args.img)
            if ig_post_id:
                results["instagram"] = ig_post_id
                print(f"[IG] Opublikowano: {ig_post_id}")
        except Exception as e:
            print(f"[IG] Blad: {e}")
    elif not args.fb_only and not ig_id:
        print("[IG] Pominięto — brak IG_ACCOUNT_ID_SACRUM w .env")

    return results


if __name__ == "__main__":
    main()
