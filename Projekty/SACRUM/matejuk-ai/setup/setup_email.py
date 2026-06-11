#!/usr/bin/env python3
"""
Interactive setup — tworzy /home/claude/.matejuk-ai/.env z App Passwords dla każdego konta Gmail.

Uruchom: python3 setup/setup_email.py
"""
import os
import sys
import imaplib
from pathlib import Path

SECRETS_DIR = Path("/home/claude/.matejuk-ai")
ENV_FILE = SECRETS_DIR / ".env"

ACCOUNTS = [
    {
        "alias": "piotr-matejuk",
        "email": "piotr.matejuk@gmail.com",
        "env_email": "GMAIL_PIOTR_EMAIL",
        "env_pass": "GMAIL_PIOTR_APP_PASSWORD",
        "imap": "imap.gmail.com",
    },
    {
        "alias": "sacrum",
        "email": "piotr@sacrum.life",
        "env_email": "GMAIL_SACRUM_EMAIL",
        "env_pass": "GMAIL_SACRUM_APP_PASSWORD",
        "imap": "imap.gmail.com",
    },
    {
        "alias": "psychedelictherapy",
        "email": "kontakt@psychedelictherapy.pl",
        "env_email": "GMAIL_PSYCHEDELIC_EMAIL",
        "env_pass": "GMAIL_PSYCHEDELIC_APP_PASSWORD",
        "imap": "imap.gmail.com",
    },
]

OPENROUTER_KEY = "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"
TELEGRAM_TOKEN = "8991731597:AAHhdAL7jExklTG99gVyvJvey0b3Qj4gy1c"
TELEGRAM_CHAT_ID = "1763598560"


def test_imap(host: str, email: str, password: str) -> bool:
    try:
        mail = imaplib.IMAP4_SSL(host)
        mail.login(email, password)
        mail.logout()
        return True
    except Exception as e:
        print(f"  ❌ Błąd: {e}")
        return False


def main():
    print("=" * 60)
    print("Matejuk AI — Setup Email")
    print("=" * 60)
    print()
    print("Potrzebuję App Password dla każdego konta Gmail.")
    print("Jak wygenerować App Password:")
    print("  1. Wejdź na: https://myaccount.google.com/apppasswords")
    print("  2. Zaloguj się na dane konto")
    print("  3. Wpisz nazwę (np. 'matejuk-ai') → Utwórz")
    print("  4. Skopiuj 16-znakowy kod (bez spacji)")
    print()

    SECRETS_DIR.mkdir(parents=True, exist_ok=True)

    # Read existing values
    existing = {}
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text().splitlines():
            if "=" in line:
                k, _, v = line.partition("=")
                existing[k.strip()] = v.strip()

    env_lines = {
        "TELEGRAM_BOT_TOKEN": existing.get("TELEGRAM_BOT_TOKEN", TELEGRAM_TOKEN),
        "TELEGRAM_CHAT_ID": existing.get("TELEGRAM_CHAT_ID", TELEGRAM_CHAT_ID),
        "OPENROUTER_API_KEY": existing.get("OPENROUTER_API_KEY", OPENROUTER_KEY),
        "EMAIL_LOOKBACK_HOURS": existing.get("EMAIL_LOOKBACK_HOURS", "24"),
        "MIN_IMPORTANCE": existing.get("MIN_IMPORTANCE", "3"),
        "MATEJUK_AI_DB": existing.get("MATEJUK_AI_DB", "/home/claude/.matejuk-ai/state.db"),
    }

    for acc in ACCOUNTS:
        print(f"\n--- {acc['email']} ---")
        current_pass = existing.get(acc["env_pass"], "")
        if current_pass:
            test = input(f"App Password już zapisany. Przetestować? (t/n) [n]: ").strip().lower()
            if test != "t":
                env_lines[acc["env_email"]] = acc["email"]
                env_lines[acc["env_pass"]] = current_pass
                continue

        while True:
            pw = input(f"App Password dla {acc['email']} (lub Enter żeby pominąć): ").strip()
            if not pw:
                print(f"  ⚠️  Pominięto {acc['email']}")
                break
            pw_clean = pw.replace(" ", "")
            print(f"  Testuję połączenie IMAP...")
            if test_imap(acc["imap"], acc["email"], pw_clean):
                print(f"  ✅ OK!")
                env_lines[acc["env_email"]] = acc["email"]
                env_lines[acc["env_pass"]] = pw_clean
                break
            else:
                retry = input("  Spróbować ponownie? (t/n) [t]: ").strip().lower()
                if retry == "n":
                    break

    # Write .env
    content = "\n".join(f"{k}={v}" for k, v in env_lines.items()) + "\n"
    ENV_FILE.write_text(content)
    ENV_FILE.chmod(0o600)

    configured = [acc for acc in ACCOUNTS if env_lines.get(acc["env_pass"])]
    print(f"\n✅ Konfiguracja zapisana: {ENV_FILE}")
    print(f"   Skonfigurowane konta: {len(configured)}/{len(ACCOUNTS)}")
    for acc in configured:
        print(f"   - {acc['email']}")

    print("\n🤖 Uruchom bota:")
    print("   python3 run_bot.py")
    print("\n📧 Testuj digest:")
    print("   python3 run_digest.py")


if __name__ == "__main__":
    main()
