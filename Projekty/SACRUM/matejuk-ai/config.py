"""
Matejuk AI — configuration loader.
Reads from /home/claude/.matejuk-ai/.env (VPS) or local .env in the repo root.
"""
import os
import sys
from pathlib import Path


def _load_env(path: Path):
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip())


# Try VPS secrets first, then local workspace .env
_load_env(Path("/home/claude/.matejuk-ai/.env"))
_load_env(Path(__file__).parent.parent.parent.parent / ".env")  # workspace root


def _req(key: str) -> str:
    val = os.environ.get(key, "")
    if not val:
        print(f"[config] BRAKUJE: {key} — uruchom setup/setup_email.py", file=sys.stderr)
    return val


TELEGRAM_BOT_TOKEN = _req("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = _req("TELEGRAM_CHAT_ID")
OPENROUTER_API_KEY = _req("OPENROUTER_API_KEY")

# Gmail accounts: list of dicts
EMAIL_ACCOUNTS = []
for _alias, _email_key, _pass_key, _imap_host in [
    ("piotr-matejuk", "GMAIL_PIOTR_EMAIL", "GMAIL_PIOTR_APP_PASSWORD", "imap.gmail.com"),
    ("sacrum", "GMAIL_SACRUM_EMAIL", "GMAIL_SACRUM_APP_PASSWORD", "imap.gmail.com"),
    ("psychedelictherapy", "GMAIL_PSYCHEDELIC_EMAIL", "GMAIL_PSYCHEDELIC_APP_PASSWORD", "imap.gmail.com"),
]:
    email = os.environ.get(_email_key, "")
    password = os.environ.get(_pass_key, "")
    if email and password:
        EMAIL_ACCOUNTS.append({
            "alias": _alias,
            "email": email,
            "password": password,
            "imap_host": _imap_host,
            "smtp_host": "smtp.gmail.com",
            "smtp_port": 587,
        })

# SQLite state DB path (on VPS)
DB_PATH = Path(os.environ.get("MATEJUK_AI_DB", "/home/claude/.matejuk-ai/state.db"))
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

# Hours of email lookback
EMAIL_LOOKBACK_HOURS = int(os.environ.get("EMAIL_LOOKBACK_HOURS", "24"))

# Minimum importance score to send to Telegram (1-5)
MIN_IMPORTANCE = int(os.environ.get("MIN_IMPORTANCE", "3"))
