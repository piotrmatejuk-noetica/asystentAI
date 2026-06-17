---
data: 2026-06-17
temat: Automatyzacje dla agenta AI (bot Telegram) — 5 projektów biznesowych
query_en: Best automations for AI Telegram bot managing multi-project business (therapeutic center, hypnotherapy school, Shopify streetwear, cultural festival, personal brand)
model: WebFetch + wiedza własna (OpenRouter klucz wygasł)
koszt: $0.00
zrodla: 12
---

# Automatyzacje dla agenta AI — Telegram bot zarządzający 5 projektami

## TLDR

Cal.com self-hosted (darmowy) lub Calendly Standard ($10/seat) to najlepsze opcje dla rezerwacji terapeutycznych — oba mają webhooks działające z botem. Instagram DM przez Graph API działa, ale wymaga trybu "human agent" dla botów (okno 7 dni od ostatniej wiadomości użytkownika). Cliniko ($45/mc) ma pełne REST API do zarządzania pacjentami i jest lepsze niż SimplePractice dla automatyzacji. n8n self-hosted to fałszywa oszczędność — licencja Business kosztuje €667/mc; Make.com od $9/mc jest tańszym middleware. smsapi.pl (0.11-0.17 PLN/SMS) jest 3x tańszy niż Twilio ($0.0457 = ~0.19 PLN) dla polskiego rynku.

---

## Raport

### 1. KALENDARZ I REZERWACJE — dla terapeuty SACRUM / PSH

**Cal.com self-hosted**
- Koszt: $0 (open-source, hostowanie na własnym VPS)
- Webhooks: tak — booking created/updated/cancelled
- HIPAA compliance: tak (plan Organizations $28/user/mc, ale self-hosted = darmowe)
- API: REST + webhooks, bot może czytać dostępność, tworzyć rezerwacje, wysyłać potwierdzenia
- Trudność implementacji: 3/5 (setup VPS, ale masz już VPS i doświadczenie)
- **Rekomendacja: CAL.COM SELF-HOSTED** — zero kosztu, pełne API, HIPAA, webhook do bota

**Calendly**
- Koszt: Free (1 event type), Standard $10/seat/mc (pełne API + webhooks)
- Webhooks: dostępne od Standard ($10/mc) — invitee.created, invitee.canceled
- API: Scheduling API od Standard, Data Deletion API (Enterprise)
- Brak HIPAA na tanich planach
- Trudność: 2/5 (gotowe, prosta konfiguracja)

**Acuity Scheduling**
- Koszt: ~$20/mc (Emerging), HIPAA $45/mc (Growing)
- API: REST API, webhooks dla appointment.scheduled/cancelled/rescheduled
- Integruje się z Stripe dla płatności przy rezerwacji
- Trudność: 2/5

**Jak to działa z botem:**
1. Klient pisze na Telegram/IG: "chcę umówić sesję"
2. Bot odpowiada linkiem do Cal.com lub pokazuje dostępne sloty przez API
3. Cal.com webhook POST do bota po potwierdzeniu rezerwacji
4. Bot wysyła przypomnienie SMS (smsapi.pl) 24h przed

**Priorytet dla Piotra: 🔴 WYSOKI** — SACRUM i Magda potrzebują tego od zaraz.

---

### 2. INSTAGRAM DM — obsługa przez API

**Instagram Graph API — Messaging**
- TAK, można odpowiadać na DM z kont biznesowych (Meta Business Account)
- Wymaga: Facebook Page + połączonego Instagram Business Account + apki Meta
- **Kluczowe ograniczenie: Human Agent Policy**
  - Bot może odpowiadać automatycznie przez 7 dni od ostatniej wiadomości użytkownika
  - Po 7 dniach bez aktywności — tylko human agent może odblokować
  - Dla "standard" messaging window: 24h od ostatniej wiadomości (jak Messenger)
  - Instagram ma "human agent" token — jeden raz możesz przełączyć na 7-dniowe okno
- Dostęp do DM API wymaga: review przez Meta (dla stron trzecich), lub przez ManyChat

**ManyChat**
- Obsługuje Instagram DM automation bez przechodzenia przez Meta review
- Koszt: Free (1,000 kontaktów), Pro od $15/mc (nielimitowane kontakty)
- Możliwości: automatyczne odpowiedzi, flow, tagowanie, integracja z webhook
- **Ograniczenie: ManyChat jest middleware** — nie kontrolujesz logiki bezpośrednio
- Dla bota AI: ManyChat API + webhook do Twojego bota = hybryda

**Najlepsza opcja dla Piotra:**
ManyChat Pro ($15/mc) + webhook do Matejuk AI. ManyChat przyjmuje DM → webhook do bota → bot generuje odpowiedź → ManyChat wysyła.

Alternatywnie: własna aplikacja Meta (wymaga review, 4-8 tygodni).

**Trudność: 3/5** (ManyChat droga prosta; własna app Meta — trudniejsza)
**Priorytet: 🟡 WAŻNY** — SACRUM i Magda bardzo skorzystają.

---

### 3. CRM DLA TERAPEUTY z REST API

**Cliniko** ✅ REKOMENDOWANE
- Koszt: $45/mc (1 praktykujący), $95/mc (2-5)
- API: pełne REST API — pacjenci, wizyty, notatki, faktury, dostępność
- Dokumentacja: https://github.com/redguava/cliniko-api
- Webhooks: brak natywnych (polling przez API)
- Działa: bot może GET /patients, POST /appointments, GET /availabilities
- Trudność: 3/5
- Uwaga: australijski produkt, ale używany globalnie

**SimplePractice**
- Koszt: $29-$99/mc
- API: ograniczone, głównie dla partnerów (wymaga osobnej umowy z Simple Practice)
- NIE nadaje się do custom bota — API nie jest publiczne
- Trudność: 5/5

**Jane App**
- Koszt: CAD $74/mc
- API: brak publicznego API
- NIE nadaje się

**TheraNest**
- Koszt: $39/mc (do 30 klientów)
- API: brak publicznego API
- NIE nadaje się

**Alternatywa: Airtable jako CRM ($20/user/mc)**
- Pełne API REST, proste CRUD
- Bot może: GET /records (lista klientów), POST /records (nowy klient), PATCH (aktualizacja)
- Nie jest stricte "terapeutycznym CRM" ale działa jako baza klientów
- HIPAA: nie (bez Enterprise)
- Trudność: 1/5

**Alternatywa: Notion API (darmowy dla podstaw)**
- Notion API: pełne CRUD na bazach danych, webhooks (w 2025 dodali)
- Bezpłatnie do ~1000 bloków per workspace
- Integracja z botem: token → API calls
- Trudność: 1/5

**Rekomendacja:** Cliniko ($45/mc) dla SACRUM (prawdziwy CRM terapeutyczny) + Notion/Airtable dla prostego śledzenia leadów dla Magdy.

**Priorytet: 🟡 WAŻNY**

---

### 4. SHOPIFY AUTOMATION — egoisnt.com

**Shopify Admin API Webhooks — co bot może robić:**

Kluczowe eventy do subskrypcji:
- `orders/create` — nowe zamówienie → bot wysyła powiadomienie na Telegram
- `orders/fulfilled` — zamówienie wysłane → automatyczny email/SMS do klienta
- `inventory_levels/update` — stan magazynowy zmieniony → alert gdy < X sztuk
- `products/update` — zmiana produktu
- `checkouts/create` — porzucony koszyk (po 1h bez finalizacji)
- `app/uninstalled` — dla własnych app

**Jak skonfigurować:**
```
POST /admin/api/2024-10/webhooks.json
{
  "webhook": {
    "topic": "orders/create",
    "address": "https://twoj-bot.ts.net/shopify-webhook",
    "format": "json"
  }
}
```

Bot na VPS (klauzule) może przyjmować te webhooki przez Tailscale Funnel.

**Shopify Flow** (wbudowany w Shopify):
- Bezpłatny dla Shopify Basic i wyższych
- Automation bez kodu: "inventory < 5 → wyślij email"
- Brak natywnej integracji z Telegram — potrzebny HTTP Action + webhook do bota

**Drop launch przez bota:**
Bot na Telegram może przez Admin API:
- Zmienić status produktu z `draft` na `active` (opublikowanie dropu)
- Ustawić datę i godzinę publikacji (`published_at`)
- Wysłać wiadomość do listy mailingowej przez MailerLite

**Trudność: 2/5** — Admin API dobrze udokumentowane, SACRUM już ma Next.js/Shopify.
**Priorytet: 🟡 WAŻNY** — szczególnie inventory alerts i drop launches.

---

### 5. GOOGLE ADS API — magdalenagajdzinska.pl

**Google Ads API możliwości:**
- Zarządzanie kampaniami: tworzenie, wstrzymywanie, modyfikacja budżetów
- Raportowanie: metryki (CPC, konwersje, CTR) przez GAQL (Google Ads Query Language)
- Automatyczne reguły: zmiana stawek, budżetów na podstawie performance
- Dostęp do kont MCC (manager account) — jeden token dla wszystkich klientów

**Wymagania Developer Token:**
- Wymagany Developer Token od Google — BEZPŁATNY, ale:
  - Test access (podstawowy): natychmiastowy, dostęp do kont testowych
  - Standard access (produkcja): wymaga aplikacji i review (2-4 tygodnie)
  - Token jest darmowy, ale trzeba mieć aktywne konto Google Ads
- Limit: 10,000 operacji/dzień (test), nieograniczone (standard)

**Alternatywy:**
- **Supermetrics** — obsługuje Google Ads, ale głównie READ (raportowanie). Brak operacji write przez MCP.
- **Optmyzr** ($208-$499/mc) — zarządzanie kampaniami, AI suggestions, drogie
- **Google Ads Scripts** — darmowe, JS, ale wymaga ręcznego uruchomienia lub harmonogramu
- **Google Ads API + Python client library** — najlepsza opcja dla bota

**Jak zintegrować z botem:**
Piotr pisze na Telegram: "Zatrzymaj kampanię Magda na weekend"
→ Bot przez Google Ads API: PATCH campaign status = PAUSED

**Trudność: 4/5** — wymaga review Googla, OAuth2, setup developer account
**Koszt: $0** (API darmowe)
**Priorytet: 🟢 NORMALNY** — Magda dopiero startuje, można dodać po uruchomieniu kampanii.

---

### 6. SMS / PRZYPOMNIENIA — Polska

**smsapi.pl** ✅ REKOMENDOWANE DLA POLSKI
- Prepaid: 0.11–0.17 PLN/SMS (zależy od kwoty doładowania)
- Postpaid: od 49 PLN/mc + 0.08–0.16 PLN/SMS
- API: REST, gotowe biblioteki PHP/Python/Java/C#
- Alphanumeric sender ID (np. "SACRUM"): dostępny
- Trudność: 1/5 — prosta integracja

**Twilio**
- SMS do Polski: $0.0457/wiadomość ≈ 0.19 PLN
- Droższy od smsapi.pl o ~70%
- Sens jeśli już używasz Twilio do innych celów (np. Verify API)
- Trudność: 2/5

**MessageBird / Vonage**
- Podobne ceny do Twilio, mniej popularne w Polsce

**Jak to działa dla SACRUM:**
1. Cliniko/Cal.com webhook 24h przed sesją → bot → smsapi.pl → SMS do klienta: "Przypomnienie: sesja jutro o 14:00"
2. Klient odpisuje SMS → smsapi.pl webhook → bot informuje Piotra na Telegram

**Priorytet: 🔴 WYSOKI** — przypomnienia o sesjach = mniej no-show, konkretny ROI.

---

### 7. FORMULARZE INTAKE — Typeform / Tally

**Tally.so** ✅ REKOMENDOWANE
- Koszt: darmowy (webhooks FREE dla wszystkich użytkowników)
- Webhook payload: pełne dane formularza w JSON — ID pola, wartość, timestamp, email
- Konfiguracja: formularz → Settings → Webhooks → URL bota
- Typy pól: tekst, email, checkbox, upload pliku, płatność, podpis
- Trudność: 1/5
- **Bonus:** Tally ma wbudowaną integrację z Notion — wyniki trafiają prosto do bazy

**Jak działa z botem:**
1. Klient wypełnia Tally (formularz intake do sesji SACRUM)
2. Tally webhook → POST do bota → bot parsuje JSON
3. Bot tworzy kartę w Notion/Cliniko + wysyła Piotrowi streszczenie na Telegram

**Typeform**
- Koszt: Free (10 odpowiedzi/mc), Basic $25/mc (webhooks), Growth $50/mc
- Webhooks od Basic ($25/mc) — droższe niż Tally za to samo
- Lepszy UX formularzy (bardziej premium look)

**Jotform**
- Koszt: Free (5 formularzy, 100 odpowiedzi), Bronze $34/mc
- API i webhooks dostępne na płatnych planach
- Mniej polecany — za dużo ograniczeń na free

**Priorytet: 🔴 WYSOKI** — SACRUM intake process powinien być zautomatyzowany od zaraz.

---

### 8. STRIPE WEBHOOKS — płatności

**Co Stripe może wysyłać do bota:**

| Event | Co robi |
|-------|---------|
| `payment_intent.succeeded` | Płatność zakończona sukcesem — potwierdź rezerwację |
| `payment_intent.payment_failed` | Płatność nieudana — wyślij alert do klienta |
| `invoice.paid` | Faktura opłacona (subskrypcja) |
| `invoice.payment_failed` | Brak płatności — triggeruj follow-up |
| `customer.subscription.created` | Nowa subskrypcja |
| `customer.subscription.deleted` | Anulowanie subskrypcji |
| `checkout.session.completed` | Zakup przez Stripe Checkout |

**Implementacja:**
1. Stripe Dashboard → Developers → Webhooks → Add endpoint → URL bota
2. Bot weryfikuje `Stripe-Signature` header (HMAC-SHA256)
3. Bot parsuje event.type i reaguje

**Dla SACRUM:** po `payment_intent.succeeded` bot może:
- Automatycznie dodać klienta do Cliniko
- Wysłać mail potwierdzający (przez MailerLite)
- Powiadomić Piotra na Telegram z detalami płatności

**Koszt Stripe:** 1.4% + €0.25 (karty europejskie). Webhooks bezpłatne.

**Trudność: 2/5** — bardzo dobrze udokumentowane.
**Priorytet: 🔴 WYSOKI** — fundament dla płatności SACRUM i PSH.

---

### 9. NOTION vs AIRTABLE jako CRM

| Kryterium | Notion | Airtable |
|-----------|--------|----------|
| Cena (free) | Free (dobre limity) | Free (1,200 rekordów/base) |
| Cena (płatny) | $10/user/mc (Plus) | $20/user/mc (Team) |
| API CRUD | TAK — pages, databases | TAK — records, fields |
| Webhooks | TAK (dodane 2025) | TAK (Automation) |
| Relacje między danymi | Dobre (linked databases) | Doskonałe (linked records) |
| Views/filtry | Dobre | Doskonałe (Grid, Kanban, Calendar) |
| Integracja z Telegram botem | Łatwa (REST + token) | Łatwa (REST + API key) |
| HIPAA | NIE (żaden plan) | NIE (bez Enterprise) |
| Najlepsze dla | Wiedza + notatki + lekkie CRM | CRM, strukturalne dane |

**Rekomendacja:**
- **Notion** → dla SACRUM jako knowledge base + lekki CRM leadów (już prawdopodobnie używasz)
- **Airtable** → dla Magdy jako CRM klientów (bardziej tabelaryczne, łatwiejsze w obsłudze przez kogoś bez doświadczenia)

Oba są znacznie prostsze do integracji z botem niż Cliniko — ale brak HIPAA to ograniczenie dla danych medycznych pacjentów.

---

### 10. n8n SELF-HOSTED vs MAKE.COM

**n8n — UWAGA: pułapka cenowa**

n8n self-hosted NIE jest darmowe dla produkcji:
- Self-hosted wymaga planu Business lub Enterprise
- **Business: €667/mc** — to jest cena za self-hosting (licencja)
- n8n Cloud: Starter €20/mc (2,500 executions), Pro €50/mc (10,000 executions)
- Community edition (bez licencji): darmowe, ale brak support, SSO, limitowane features

**Werdykt n8n:** dla 5 projektów Piotra n8n Community Edition na VPS może wystarczyć (brak licencji = tylko podstawowe features), ale to dług techniczny. Dla produkcji — za drogi.

**Make.com** ✅ REKOMENDOWANE jako middleware
- Free: 1,000 operacji/mc (wystarczy do testów)
- Core: $9/mc (10,000 operacji) — dla małego biznesu wystarczy
- Pro: $16/mc (10,000 + priority + full logs)
- 3,000+ integracji
- Cena za operację (każdy moduł = 1 operacja), nie za execution

**Porównanie dla Piotra:**

| Aspekt | n8n Community (VPS) | Make.com Core ($9/mc) |
|--------|--------------------|-----------------------|
| Koszt | $0 licencja + VPS | $9/mc |
| Setup | Wysoki (Docker, konfiguracja) | Minuty (GUI) |
| Integracje | 400+ nodes | 3,000+ |
| Support | Forum | Email |
| Stabilność | Twoja odpowiedzialność | Managed |
| Logs | Limitowane | Pełne (Pro) |

**Rekomendacja:** Make.com Core ($9/mc) jako middleware zamiast n8n — tańszy realnie (bez czasu na utrzymanie VPS n8n), więcej integracji, zero konfiguracji.

Ale: skoro masz VPS z Tailscale i Docker-doświadczenie, **n8n Community na VPS** dla prostych flow (Shopify → Telegram, Tally → Notion) jest rozsądną opcją zerowego kosztu.

---

## Podsumowanie — Mapa implementacji

### Faza 1 — Natychmiast (koszt: ~$60-80/mc)
| Narzędzie | Projekt | Koszt | Działanie |
|-----------|---------|-------|-----------|
| Cal.com self-hosted | SACRUM + Magda | $0 | Bookowanie sesji, webhooks do bota |
| Tally.so (darmowy) | SACRUM | $0 | Intake formularze → bot → Notion |
| Stripe webhooks | SACRUM + PSH | $0 (API) | Potwierdzenia płatności → bot |
| smsapi.pl | SACRUM + Magda | ~$20/mc | Przypomnienia SMS o sesjach |
| Shopify webhooks | egoisnt.com | $0 (API) | Alerty orders/inventory → bot |

### Faza 2 — W ciągu miesiąca (dodatkowe ~$60/mc)
| Narzędzie | Projekt | Koszt | Działanie |
|-----------|---------|-------|-----------|
| ManyChat Pro | SACRUM + Magda | $15/mc | Instagram DM → webhook → bot |
| Cliniko | SACRUM | $45/mc | CRM terapeutyczny z pełnym API |
| Make.com Core | All | $9/mc | Middleware dla flow cross-projektowych |

### Faza 3 — Gdy kampanie Magdy startują
| Narzędzie | Projekt | Koszt | Działanie |
|-----------|---------|-------|-----------|
| Google Ads API | Magda | $0 (API) | Zarządzanie kampaniami przez bota |

---

## Źródła

1. https://cal.com/pricing
2. https://calendly.com/pages/pricing
3. https://www.cliniko.com/pricing/
4. https://shopify.dev/docs/api/admin-rest/2024-10/resources/webhook
5. https://tally.so/help/webhooks
6. https://n8n.io/pricing/
7. https://www.twilio.com/en-us/sms/pricing/pl
8. https://smsapi.pl/cennik
9. https://developers.google.com/google-ads/api/docs/start
10. https://docs.stripe.com/webhooks
11. https://developers.notion.com/docs/getting-started
12. https://airtable.com/pricing
13. https://www.make.com/en/pricing

---

*Wygenerowano: 2026-06-17 | Koszt: $0.00 | Źródła: 13 | Metoda: WebFetch + wiedza własna*
