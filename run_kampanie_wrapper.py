#!/usr/bin/env python3
"""
Wrapper do kampanie-report skill — uruchamiany przez Claude Cron lub ręcznie.
Ten skrypt nie odpytuje Supermetrics bezpośrednio — to robi Claude Desktop (MCP).
Zamiast tego: czyta daily-report.md i wysyła na Telegram.
"""
import os
import sys
import urllib.request
import urllib.parse
import json
from pathlib import Path
from datetime import datetime

VAULT = Path(__file__).parent
REPORT_FILE = VAULT / "Projekty/SACRUM/kampanie/daily-report.md"


def load_env():
    env_file = VAULT / ".env"
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            if "=" in line and not line.startswith("#"):
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())


def send_telegram(text: str):
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        print("Brak TELEGRAM_BOT_TOKEN lub TELEGRAM_CHAT_ID")
        return

    data = json.dumps({"chat_id": chat_id, "text": text, "parse_mode": "HTML"}).encode()
    req = urllib.request.Request(
        f"https://api.telegram.org/bot{token}/sendMessage",
        data=data,
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        result = json.loads(resp.read())
        if not result.get("ok"):
            print(f"Telegram error: {result}")


def main():
    load_env()
    if not REPORT_FILE.exists():
        send_telegram("⚠️ Brak raportu kampanii — uruchom /kampanie-report w Claude Desktop.")
        return

    content = REPORT_FILE.read_text()
    today = datetime.now().strftime("%Y-%m-%d")

    # sprawdź czy raport jest aktualny (z dzisiaj)
    if today not in content and "--" not in content:
        send_telegram(f"⚠️ Raport kampanii może być nieaktualny (nie zawiera daty {today}).")

    # wyślij raport na Telegram
    send_telegram(content[:3800])
    print("Raport wysłany.")


if __name__ == "__main__":
    main()
