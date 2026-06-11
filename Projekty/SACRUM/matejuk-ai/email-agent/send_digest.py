"""Main digest script — fetch → filter → save to DB → send to Telegram."""
import sys
import time

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent.parent))

from config import MIN_IMPORTANCE, TELEGRAM_CHAT_ID
from shared.claude_client import filter_email
from shared.telegram_sender import send_message, email_keyboard, format_email_message
from shared.state_db import save_email, get_email, update_email
from imap_client import fetch_all_accounts


def run_digest(lookback_hours: int = None):
    print("[digest] Start")
    emails = fetch_all_accounts()
    print(f"[digest] Łącznie: {len(emails)} nieprzeczytanych")

    sent = 0
    for mail in emails:
        # Skip already processed
        existing = get_email(mail["id"])
        if existing and existing["status"] in ("sent", "skipped", "replied"):
            continue

        print(f"[digest] Filtruję: {mail['subject'][:50]}")
        try:
            analysis = filter_email(mail["from_addr"], mail["subject"], mail["body"])
        except Exception as e:
            print(f"[digest] Błąd filtrowania: {e}")
            continue

        importance = int(analysis.get("importance", 1))
        if importance < MIN_IMPORTANCE:
            print(f"[digest] Pominięto (ważność {importance}): {mail['subject'][:40]}")
            continue

        draft = analysis.get("draft") or ""
        data = {
            "id": mail["id"],
            "account": mail["account"],
            "from_addr": mail["from_addr"],
            "subject": mail["subject"],
            "body": mail["body"],
            "draft": draft,
            "importance": importance,
            "category": analysis.get("category", "inne"),
            "project": analysis.get("project", "inne"),
        }
        save_email(data)

        text = format_email_message(
            account=mail["account"],
            project=analysis.get("project", "inne"),
            category=analysis.get("category", "inne"),
            subject=mail["subject"],
            from_addr=mail["from_addr"],
            snippet=mail["body"][:300],
            draft=draft,
            importance=importance,
        )

        try:
            result = send_message(text, reply_markup=email_keyboard(mail["id"]))
            msg_id = result.get("result", {}).get("message_id")
            if msg_id:
                update_email(mail["id"], message_id=msg_id)
            sent += 1
        except Exception as e:
            print(f"[digest] Błąd Telegrama: {e}")

        time.sleep(0.5)  # rate limit

    if sent == 0:
        send_message("📭 Brak nowych ważnych wiadomości.")
    else:
        print(f"[digest] Wysłano {sent} wiadomości do Telegrama")


if __name__ == "__main__":
    run_digest()
