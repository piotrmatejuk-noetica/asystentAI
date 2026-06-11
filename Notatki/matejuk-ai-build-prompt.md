# Matejuk AI — Prompt Budowania Wirtualnej Asystentki

> Wklej ten prompt na początku nowej sesji Claude Code w tym workspace.

---

## KONTEKST

Budujesz Matejuk AI — wirtualną asystentkę Piotra Matejuka działającą 24/7 na VPS (5.180.180.200). Piotr prowadzi 5 projektów jednocześnie (SACRUM, hipnoterapia.edu.pl, egoisnt.com, cienfestiwal.com, magdalenagajdzinska.pl). Ma 3 skrzynki email, WhatsAppa i Google Calendar — i jest zawalony wiadomościami. Twoim zadaniem jest zbudować system który:

1. Czyta wszystkie wiadomości (email + WhatsApp)
2. Filtruje ważne od szumu (memy, "co tam", casual)
3. Drafuje odpowiedzi w głosie Piotra
4. Wysyła digest do Telegrama (bot już działa 24/7 na VPS)
5. Piotr klika "wyślij" lub edytuje — bez otwierania skrzynek

## INFRASTRUKTURA (już istnieje)

- **VPS:** 5.180.180.200, user root, workspace `/home/claude/vault-git`
- **Claude user na VPS:** zalogowany, uruchamia joby
- **Claude Cron:** działa na VPS, dashboard `http://100.120.58.26:7777`
- **Telegram bot:** sparowany z Piotrem (ID: 1763598560), działa 24/7
- **Workspace Obsidian:** `/Users/piotrmatejuk/Desktop/PiotrekMate` (Mac) = `/home/claude/vault-git` (VPS)
- **Google Drive MCP:** podłączony
- **Stack:** Node.js 22, Python 3, Claude Code CLI

## FAZA 1 — EMAIL (zacznij tu)

### Konta Gmail
- `piotr.matejuk@gmail.com` — osobiste + SACRUM
- `piotr@sacrum.life` — SACRUM (Google Workspace)
- `kontakt@psychedelictherapy.pl` — zapytania klientów

### Co zbudować

**Skrypt: `Projekty/SACRUM/matejuk-ai/email-agent/fetch_emails.py`**

Używa Gmail API (googleapis Python) do pobierania nieprzeczytanych wiadomości z ostatnich 24h z każdego konta. Output: JSON z listą wiadomości (`id`, `from`, `subject`, `body_snippet`, `date`, `account`).

**Autentykacja:**
- OAuth2 per konto (credentials.json + token.json per konto)
- Przy pierwszym uruchomieniu: `python fetch_emails.py --setup --account piotr.matejuk` → otwiera browser → user klika
- Tokeny przechowywane w `.secrets/gmail/` (NIE commitować do gita)

**Skrypt: `email-agent/filter_emails.py`**

Wywołuje Claude API (Haiku — tani i szybki) na każdej wiadomości z promptem:

```
Kontekst: Piotr Matejuk, hipnoterapeuta, prowadzi SACRUM (centrum terapii psychodelicznych), PSH, egoisnt.com, festiwal Cień.

Wiadomość:
Od: {from}
Temat: {subject}
Treść: {body}

Oceń:
1. WAŻNOŚĆ (1-5): 1=spam/meme/casual, 3=info, 5=wymaga odpowiedzi/jest pilne
2. KATEGORIA: klient|partnerstwo|media|admin|osobiste|spam
3. PROJEKT: SACRUM|PSH|egoisnt|Cień|Magda|osobiste|inne
4. DRAFT_ODPOWIEDZI: (tylko jeśli ważność >= 3) — krótka odpowiedź w stylu Piotra, bezpośrednia, bez korporacyjnego języka
5. UZASADNIENIE: jednozdaniowe dlaczego taka ocena

Zwróć JSON.
```

Filtruj: `ważność >= 3` idzie do Telegrama.

**Skrypt: `email-agent/send_digest.py`**

Wysyła przez Telegram Bot API do ID 1763598560. Format wiadomości Telegram:

```
📧 [SACRUM] Zapytanie o terapię
Od: jan.kowalski@gmail.com
---
Dzień dobry, chciałem zapytać o...

💬 Draft odpowiedzi:
Cześć Jan, dzięki za wiadomość. Możemy się umówić na rozmowę wstępną w...

[✅ Wyślij draft] [✏️ Edytuj] [🗑️ Pomiń]
```

Telegram inline keyboard — przyciski callbackowe.

**Webhook handler: `email-agent/telegram_webhook.py`** (Flask/FastAPI, port 3477)

Obsługuje kliknięcia przycisków:
- `Wyślij draft` → wysyła email przez Gmail API
- `Edytuj` → czeka na kolejną wiadomość od Piotra jako treść, potem wysyła
- `Pomiń` → archiwizuje

---

## FAZA 2 — WHATSAPP

Użyj `whatsapp-web.js` (Node.js, nieoficjalne ale sprawdzone):

```bash
cd Projekty/SACRUM/matejuk-ai/whatsapp-agent
npm init -y && npm install whatsapp-web.js qrcode-terminal
```

**`whatsapp_agent.js`:**
- Przy starcie: jeśli brak sesji → wydrukuj QR do terminala (Piotr skanuje raz)
- Sesja zapisywana lokalnie (`.wwebjs_auth/`)
- Nasłuchuje nowych wiadomości
- Filtruje przez Claude API (analogicznie do email)
- Wysyła ważne do Telegrama z draftem
- Obsługuje callback z Telegrama → wysyła odpowiedź na WhatsApp

**Ważne:** whatsapp-web.js wymaga Chromium. Na VPS: `apt install chromium-browser`.

---

## FAZA 3 — GOOGLE CALENDAR

**`calendar-agent/calendar_sync.py`:**

Używa Google Calendar API:
- Pobiera eventy na najbliższe 7 dni
- Przy porannym digest (07:00) wysyła do Telegrama plan dnia
- Umożliwia tworzenie eventów przez Telegrama: Piotr pisze "umów mnie z Janem Kowalskim w piątek o 14:00" → agent tworzy event i potwierdza
- Parsowanie dat przez Claude

---

## FAZA 4 — GOOGLE DRIVE + PLIKI LOKALNE

Agent ma dostęp do:
- Google Drive (MCP już podłączony, użyj `mcp__claude_ai_Google_Drive__*` tools w skryptach Claude)
- Lokalny workspace: `/Users/piotrmatejuk/Desktop/PiotrekMate` (Mac) lub `/home/claude/vault-git` (VPS)

Możliwości:
- "Znajdź kontrakt z Adamem z maja" → przeszukuje Drive + Obsidian vault
- "Przygotuj ofertę dla nowego klienta na podstawie szablonu" → czyta szablon z Drive/vault, generuje
- "Dodaj notatkę ze spotkania" → tworzy plik w `Notatki/spotkania/`

---

## HARMONOGRAM (Claude Cron)

Po zbudowaniu, skonfiguruj te joby przez API `http://100.120.58.26:7777`:

| Job | Cron | Opis |
|-----|------|------|
| email-morning | `0 7 * * *` | Poranny digest: email + plan dnia |
| email-check | `0 */2 * * *` | Co 2h: nowe maile |
| whatsapp-agent | systemd/pm2 | Ciągły (event-driven) |
| calendar-evening | `0 20 * * *` | Wieczorny przegląd jutrzejszego dnia |

---

## KOLEJNOŚĆ BUDOWANIA

1. **Gmail fetch + filter** (1 konto testowo: piotr.matejuk@gmail.com)
2. **Telegram digest** z przyciskami
3. **Gmail OAuth setup** dla pozostałych 2 kont
4. **Telegram webhook** + obsługa "wyślij draft"
5. **WhatsApp agent** (QR setup interaktywny)
6. **Calendar integration**
7. **Drive/plik search** przez Telegram ("znajdź X")
8. **Claude Cron jobs** na VPS

## PLIKI I STRUKTURA

```
Projekty/SACRUM/matejuk-ai/
├── .secrets/               # NIE commitować (w .gitignore)
│   ├── gmail/
│   │   ├── piotr-matejuk-credentials.json
│   │   ├── piotr-matejuk-token.json
│   │   ├── sacrum-credentials.json
│   │   └── psychedelictherapy-credentials.json
│   └── telegram_token.txt
├── email-agent/
│   ├── fetch_emails.py
│   ├── filter_emails.py
│   └── send_digest.py
├── whatsapp-agent/
│   ├── whatsapp_agent.js
│   └── package.json
├── calendar-agent/
│   └── calendar_sync.py
├── telegram-bot/
│   ├── webhook_handler.py
│   └── keyboards.py
├── shared/
│   ├── claude_client.py    # Claude API wrapper (Haiku dla filtrowania, Sonnet dla drafts)
│   ├── telegram.py         # Telegram sender utility
│   └── config.py           # Ścieżki, stałe
└── README.md
```

## GŁOS PIOTRA W DRAFTACH

Prompt systemowy dla Claude przy generowaniu drafów:

```
Piszesz w imieniu Piotra Matejuka — hipnoterapeuty, psychotraumatologu, prowadzącego SACRUM (centrum terapii psychodelicznych) i Profesjonalną Szkołę Hipnoterapii.

Styl: bezpośredni, ciepły ale konkretny, bez korporacyjnego języka. Nie używaj "Z wyrazami szacunku" — raczej "Pozdrawiam" lub imię. Krótko. Pierwsze zdanie to odpowiedź, nie wstęp.

Kontekst: {kontekst_wiadomości}
```

## FILTR WAŻNOŚCI — REGUŁY

Automatycznie odrzucaj (ważność 1-2):
- Wiadomości z "unsubscribe" w stopce (newsletter)
- Nadawca: mailer-daemon, noreply, donotreply
- Temat zawiera: "oferta", "promocja", "newsletter", "automatyczna odpowiedź"
- Treść to forward łańcuszkowy lub GIF/mem bez kontekstu
- Pytania czysto towarzyskie bez action items od osób niebiznesowych

Zawsze ważne (ważność 4-5):
- Klienci SACRUM pytający o terapię
- Nowe płatności/faktury
- Partnerzy biznesowi
- Media/dziennikarze
- Piotr wymieniony z imienia lub nazwiska
- Cokolwiek z "pilne", "deadline", "umowa"

---

## ZACZNIJ OD

```bash
# Sprawdź co już istnieje
ls Projekty/SACRUM/matejuk-ai/ 2>/dev/null || echo "puste — zaczynam od zera"

# Zainstaluj Gmail API
pip3 install google-auth-oauthlib google-auth-httplib2 google-api-python-client

# Utwórz strukturę
mkdir -p Projekty/SACRUM/matejuk-ai/{email-agent,whatsapp-agent,calendar-agent,telegram-bot,shared,.secrets/gmail}
echo ".secrets/" >> .gitignore
```

Potem zapytaj Piotra o credentials.json z Google Cloud Console (Gmail API + Calendar API muszą być włączone w projekcie GCP).
