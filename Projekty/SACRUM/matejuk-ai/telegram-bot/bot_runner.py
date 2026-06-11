"""Telegram bot — long-polling loop. Handles button callbacks and text replies."""
import sys
import time
import traceback

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent.parent))

from config import TELEGRAM_CHAT_ID
from shared.claude_client import improve_draft
from shared.telegram_sender import get_updates, answer_callback, send_message, edit_message, email_keyboard
from shared.state_db import get_email, update_email, get_bot_state, set_bot_state
sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent.parent / "email-agent"))
from imap_client import send_reply


def handle_callback(query: dict):
    qid = query["id"]
    data = query.get("data", "")
    chat_id = str(query["message"]["chat"]["id"])
    message_id = query["message"]["message_id"]

    if not data or ":" not in data:
        answer_callback(qid, "Nieznana akcja")
        return

    action, email_id = data.split(":", 1)
    mail = get_email(email_id)
    if not mail:
        answer_callback(qid, "Email nie znaleziony (już przetworzony?)")
        return

    if action == "send":
        draft = mail.get("draft", "")
        if not draft:
            answer_callback(qid, "Brak draftu — użyj ✏️ Edytuj")
            return
        try:
            send_reply(
                account_alias=mail["account"],
                to_addr=mail["from_addr"],
                subject=mail["subject"],
                body=draft,
            )
            update_email(email_id, status="replied")
            answer_callback(qid, "✅ Wysłano!")
            edit_message(message_id, f"✅ <b>WYSŁANO</b>\n\nDo: {mail['from_addr']}\nTemat: {mail['subject']}\n\n{draft[:300]}", chat_id=chat_id)
        except Exception as e:
            answer_callback(qid, f"Błąd: {e}")

    elif action == "edit":
        set_bot_state(chat_id, "editing", {"email_id": email_id, "message_id": message_id})
        answer_callback(qid, "Napisz zmiany...")
        send_message("✏️ Napisz co zmienić w drafcie (np. 'zaproponuj piątek rano') lub wklej całą treść odpowiedzi:", chat_id=chat_id)

    elif action == "skip":
        update_email(email_id, status="skipped")
        answer_callback(qid, "🗑️ Pominięto")
        edit_message(message_id, f"🗑️ <i>Pominięto: {mail['subject']}</i>", chat_id=chat_id)


def handle_message(message: dict):
    chat_id = str(message["chat"]["id"])
    text = message.get("text", "")

    if not text:
        return

    # Commands
    if text == "/start":
        send_message("👋 Matejuk AI aktywny.\n\n/status — status systemu\n/digest — sprawdź maile teraz", chat_id=chat_id)
        return

    if text == "/status":
        from config import EMAIL_ACCOUNTS
        accounts = ", ".join(a["alias"] for a in EMAIL_ACCOUNTS) if EMAIL_ACCOUNTS else "⚠️ BRAK KONT (skonfiguruj .env)"
        send_message(f"✅ Bot działa\n📧 Konta: {accounts}", chat_id=chat_id)
        return

    if text == "/digest":
        send_message("🔄 Uruchamiam digest...", chat_id=chat_id)
        try:
            from email_agent.send_digest import run_digest
            run_digest()
        except Exception as e:
            send_message(f"❌ Błąd: {e}", chat_id=chat_id)
        return

    # Handle editing state
    state, ctx = get_bot_state(chat_id)
    if state == "editing":
        email_id = ctx.get("email_id")
        msg_id = ctx.get("message_id")
        mail = get_email(email_id)
        if not mail:
            send_message("Ups, email już nie istnieje.", chat_id=chat_id)
            set_bot_state(chat_id, "idle")
            return

        send_message("⏳ Poprawiam draft...", chat_id=chat_id)
        try:
            original = f"Od: {mail['from_addr']}\nTemat: {mail['subject']}\n\n{mail['body'][:500]}"
            new_draft = improve_draft(original, mail.get("draft", ""), text)
            update_email(email_id, draft=new_draft)
            set_bot_state(chat_id, "idle")

            send_message(
                f"✏️ <b>Poprawiony draft:</b>\n\n{new_draft}\n\n<i>Temat: {mail['subject']}</i>",
                chat_id=chat_id,
                reply_markup=email_keyboard(email_id),
            )
        except Exception as e:
            send_message(f"❌ Błąd: {e}", chat_id=chat_id)
            set_bot_state(chat_id, "idle")


def run_forever():
    print("[bot] Start — polling Telegram...")
    offset = 0
    while True:
        try:
            updates = get_updates(offset=offset, timeout=30)
            for upd in updates:
                offset = max(offset, upd["update_id"] + 1)
                if "callback_query" in upd:
                    handle_callback(upd["callback_query"])
                elif "message" in upd:
                    msg = upd["message"]
                    chat_id = str(msg.get("chat", {}).get("id", ""))
                    # only respond to Piotr
                    if chat_id == TELEGRAM_CHAT_ID:
                        handle_message(msg)
        except KeyboardInterrupt:
            print("[bot] Stop")
            break
        except Exception:
            print(f"[bot] Błąd:\n{traceback.format_exc()}")
            time.sleep(5)


if __name__ == "__main__":
    run_forever()
