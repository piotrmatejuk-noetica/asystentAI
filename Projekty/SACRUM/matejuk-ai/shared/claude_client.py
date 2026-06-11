"""Claude via OpenRouter — haiku for filtering (cheap), sonnet for drafts."""
import json
import sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent.parent))

import httpx
from config import OPENROUTER_API_KEY

_BASE = "https://openrouter.ai/api/v1/chat/completions"
_HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://sacrum.life",
    "X-Title": "Matejuk AI",
}

HAIKU = "anthropic/claude-haiku-4-5"
SONNET = "anthropic/claude-sonnet-4-6"


def chat(messages: list[dict], model: str = HAIKU, temperature: float = 0.3) -> str:
    resp = httpx.post(
        _BASE,
        headers=_HEADERS,
        json={"model": model, "messages": messages, "temperature": temperature},
        timeout=60,
    )
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"].strip()


FILTER_SYSTEM = """Jesteś asystentem Piotra Matejuka — hipnoterapeuty, psychotraumatologu, prowadzącego SACRUM (centrum terapii psychodelicznych), Profesjonalną Szkołę Hipnoterapii, egoisnt.com, festiwal Cień.

Oceniasz wiadomości email. Zwróć WYŁĄCZNIE poprawny JSON (bez markdown, bez komentarzy):

{
  "importance": 1-5,
  "category": "klient|partnerstwo|media|admin|osobiste|spam",
  "project": "SACRUM|PSH|egoisnt|Cien|Magda|osobiste|inne",
  "draft": "krótka odpowiedź w głosie Piotra (tylko jeśli importance >= 3, inaczej null)",
  "reason": "jedno zdanie uzasadnienie"
}

Skala ważności:
1 = spam/newsletter/meme/casual
2 = info, nie wymaga odpowiedzi
3 = warto przeczytać, możliwa odpowiedź
4 = ważne, wymaga odpowiedzi
5 = pilne — klient, płatność, deadline

Automatycznie 1-2: unsubscribe w stopce, noreply@, "oferta", "promocja", forward łańcuszkowy, memy.
Automatycznie 4-5: zapytania o terapię SACRUM, płatności, partnerzy biznesowi, media, "pilne"/"deadline"/"umowa"."""

VOICE_SYSTEM = """Piszesz w imieniu Piotra Matejuka — hipnoterapeuty prowadzącego SACRUM.
Styl: bezpośredni, ciepły ale konkretny, bez korporacyjnego języka.
NIE "Z wyrazami szacunku" — raczej "Pozdrawiam" lub samo imię.
Pierwsze zdanie to odpowiedź, nie wstęp. Krótko."""


def filter_email(from_addr: str, subject: str, body: str) -> dict:
    prompt = f"Od: {from_addr}\nTemat: {subject}\nTreść (fragment):\n{body[:800]}"
    result = chat([
        {"role": "system", "content": FILTER_SYSTEM},
        {"role": "user", "content": prompt},
    ], model=HAIKU)
    try:
        return json.loads(result)
    except json.JSONDecodeError:
        start = result.find("{")
        end = result.rfind("}") + 1
        return json.loads(result[start:end]) if start >= 0 else {"importance": 1, "reason": "parse error"}


def improve_draft(original_email: str, draft: str, piotr_edit: str) -> str:
    """Rewrite draft based on Piotr's edit instructions."""
    return chat([
        {"role": "system", "content": VOICE_SYSTEM},
        {"role": "user", "content": f"Oryginalna wiadomość:\n{original_email}\n\nDraft:\n{draft}\n\nPiotr chce zmienić:\n{piotr_edit}\n\nNapisz poprawiony draft."},
    ], model=SONNET)
