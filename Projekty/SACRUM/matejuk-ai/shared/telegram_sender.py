"""Telegram Bot API wrapper — send messages and handle inline keyboards."""
import sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent.parent))

import httpx
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

_BASE = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"


def _post(method: str, **kwargs) -> dict:
    resp = httpx.post(f"{_BASE}/{method}", json=kwargs, timeout=30)
    resp.raise_for_status()
    return resp.json()


def send_message(text: str, chat_id: str = None, reply_markup: dict = None) -> dict:
    params = {"chat_id": chat_id or TELEGRAM_CHAT_ID, "text": text, "parse_mode": "HTML"}
    if reply_markup:
        params["reply_markup"] = reply_markup
    return _post("sendMessage", **params)


def edit_message(message_id: int, text: str, chat_id: str = None, reply_markup: dict = None) -> dict:
    params = {"chat_id": chat_id or TELEGRAM_CHAT_ID, "message_id": message_id, "text": text, "parse_mode": "HTML"}
    if reply_markup:
        params["reply_markup"] = reply_markup
    return _post("editMessageText", **params)


def answer_callback(callback_query_id: str, text: str = "") -> dict:
    return _post("answerCallbackQuery", callback_query_id=callback_query_id, text=text)


def get_updates(offset: int = 0, timeout: int = 30) -> list[dict]:
    result = _post("getUpdates", offset=offset, timeout=timeout, allowed_updates=["message", "callback_query"])
    return result.get("result", [])


def email_keyboard(email_id: str) -> dict:
    """Inline keyboard for an email digest item."""
    return {
        "inline_keyboard": [[
            {"text": "✅ Wyślij draft", "callback_data": f"send:{email_id}"},
            {"text": "✏️ Edytuj", "callback_data": f"edit:{email_id}"},
            {"text": "🗑️ Pomiń", "callback_data": f"skip:{email_id}"},
        ]]
    }


def format_email_message(account: str, project: str, category: str,
                          subject: str, from_addr: str, snippet: str,
                          draft: str, importance: int) -> str:
    imp_emoji = {5: "🔴", 4: "🟠", 3: "🟡"}.get(importance, "⚪")
    lines = [
        f"{imp_emoji} <b>[{project.upper()}] {subject}</b>",
        f"<i>Od: {from_addr}</i>  •  <i>{account}</i>",
        "",
        snippet[:300],
    ]
    if draft:
        lines += ["", "💬 <b>Draft odpowiedzi:</b>", draft[:500]]
    return "\n".join(lines)
