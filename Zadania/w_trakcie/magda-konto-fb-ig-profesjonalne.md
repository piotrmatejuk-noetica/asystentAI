---
status: w_trakcie
priorytet: pilne
termin:
utworzone: 2026-06-21
projekt: "[[Zadania/projekty/Magda]]"
rodzic:
---

# Magda — konto profesjonalne FB i IG + pierwsze 10 postów

## Cel

Założyć profesjonalne konta Facebooka i Instagrama dla Magdaleny Gajdzińskiej pod nazwą **"Magdalena Gajdzińska — Hipnoza Oddech Integracja"**, podpiąć je pod portfolio Piotrek Mate (zarządzanie), nadać uprawnienia admin dla `mlle.madeleine@gmail.com`, połączyć z magda-agentem (Telegram bot) i przygotować plan pierwszych 10 postów/reelsów.

## Kontekst

Magda nie ma jeszcze kont biznesowych. Cały marketing prowadzi Piotr. Bot @MagdaMarketingBot (port 8000 na Macu) jest gotowy — brakuje tylko podpięcia FB Page token (blokada opisana w NOW.md). To zadanie zamyka ten ostatni krok.

## Podzadania

- [ ] **FB — Utwórz Stronę** pod kontem borsuk1916@gmail.com (konto Magdy)
  - Nazwa: `Magdalena Gajdzińska — Hipnoza Oddech Integracja`
  - Kategoria: `Health/Beauty` lub `Hypnotherapist`
  - Dodaj jako admin: `mlle.madeleine@gmail.com`
  - Dodaj Piotrka jako admin (konto piotr.matejuk@gmail.com lub przez Business Portfolio)

- [ ] **IG — Utwórz konto profesjonalne** (lub przekształć istniejące prywatne)
  - Typ konta: Creator lub Business
  - Połącz z FB Page powyżej
  - Username: `magdalenagajdzinska` lub `magdalena.gajdzinska.hipnoza`

- [ ] **FB Business Portfolio (Piotrek Mate)**
  - Dodaj nową FB Page do portfolio Piotrek Mate → [business.facebook.com](https://business.facebook.com)
  - Przypisz Piotrka jako admin → zarządzanie bez logowania na konto Magdy

- [ ] **OAuth dla magda-agenta**
  1. Dodaj `borsuk1916@gmail.com` jako Developer/Tester w FB Developer Console:
     `https://developers.facebook.com/apps/937795249248975/roles/roles/`
  2. Zaloguj się jako `borsuk1916@gmail.com` i otwórz OAuth URL:
     `https://www.facebook.com/v20.0/dialog/oauth?client_id=937795249248975&redirect_uri=https%3A%2F%2Fklauzule.tail4676a1.ts.net%2Fmeta%2Foauth&scope=pages_manage_posts%2Cpages_show_list%2Cpages_read_engagement%2Cinstagram_basic%2Cinstagram_content_publish&response_type=code`
  3. `magda-oauth.service` jest aktywny na VPS (port 8789) — token trafi automatycznie do bota

- [ ] **Test połączenia** — wyślij post testowy przez @MagdaMarketingBot (`/post`)

## Propozycja pierwszych 10 postów/reelsów

Głos: Magdalena. Styl: osobisty, konkretny, bez coachingowego bla bla. Profil: hipnoterapeutka + oddech + integracja.

---

**1. POST — Intro (karuzelka lub reel)**
*"Hipnoza to nie sztuczka."*
Krótko kim jestem i czym się zajmuję. Jedno zdanie na slajd. Bez CV, bez dyplomów — tylko: z jakimi problemami przychodzą do mnie ludzie i co się zmienia.

---

**2. REEL — Oddech jako narzędzie**
*"Oddech to jedyna funkcja autonomiczna, którą możesz świadomie kontrolować."*
30 sekund: pokaż jeden prosty wzorzec oddechowy. Na koniec — co zmienia się w ciele.

---

**3. POST — Obalenie mitu**
*"Nie, nie mogę Cię zahipnotyzować wbrew Twojej woli."*
Trzy największe mity o hipnozie. Każdy obalony w jednym zdaniu. Bez tłumaczeń — teza i kontra.

---

**4. REEL — Sesja od kuchni**
Jak wygląda prawdziwa sesja hipnoterapeutyczna. Bez dramatycznych efektów specjalnych. Krzesło, słowa, cisza. Co faktycznie się dzieje — opowiada Magda wprost do kamery.

---

**5. POST — Case study (anonimowy)**
*"Osoba z lękiem lotniczym. 3 lata omijania samolotów. 2 sesje."*
Konkretna historia, konkretny efekt, zero sensacji. Format: problem → podejście → wynik.

---

**6. REEL — Czym jest integracja**
*"Terapia nie kończy się na sesji."*
Co to znaczy integrować doświadczenie — oddech, ruch, codzienność. 45 sekund, bez slajdów.

---

**7. POST — Pytania i odpowiedzi**
Zbierz 3 pytania które dostajesz najczęściej. Odpowiedź pod każdym: 2-3 zdania, precyzyjnie.

---

**8. REEL — Praca z ciałem**
Pokaż jeden prosty protokół pracy z napięciem somatycznym. Nagranie przy biurku/w gabinecie. Instrukcja krok po kroku — możliwa do zrobienia samemu.

---

**9. POST — Dlaczego wybrałam tę pracę**
Nie motywacyjny. Jeden konkretny moment który zdecydował. Prawdziwa historia, bez upiększeń.

---

**10. REEL — Co to znaczy "bezpieczna przestrzeń"**
*"Nie mówię tego żeby brzmiało dobrze."*
Co konkretnie robisz żeby sesja była bezpieczna — nie jako hasło marketingowe, ale jako praktyka. Pokaż gabinetowe detale.

---

## Powiązania

- Projekt: [[Zadania/projekty/Magda]]
- Bot: @MagdaMarketingBot (LaunchAgent port 8000)
- Repo: piotrmatejuk-noetica/magda-agent
- Blokada NOW.md: FB Page token → borsuk1916@gmail.com

## Notatki

**Dane konta Magdy:** borsuk1916@gmail.com
**FB App ID:** 937795249248975
**MailerLite group Magda:** ID 190688211489523110
**magda-oauth.service:** aktywny na VPS, port 8789 przez Tailscale Funnel

---

*Utworzono: 2026-06-21*
