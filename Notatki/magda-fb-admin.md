# Magda FB Admin — status połączenia

*Aktualizacja: 2026-06-19*

## Co jest gotowe

- `magda-oauth.service` ✅ działa na VPS (port 8789, active running od 10:36)
- Tailscale Funnel ✅ `https://klauzule.tail4676a1.ts.net` → `localhost:8789` (wszystko, w tym `/meta/oauth`)
- Handler `/meta/oauth` ✅ poprawny — wymienia kod na token, szuka strony Magdy (ID: 61561269893962), wysyła token do magda-agent na Macu

## Nowe: Piotr admin strony Magdy

- Konto: **Piotrek Mate** (`borsuk1916@gmail.com`)
- Rola: **Administrator** strony Magdalena Gajdzińska (FB page ID: 61561269893962)

## Co MUSI zrobić Piotr (1 krok)

**Problem:** FB app 937795249248975 jest w trybie Development — tylko użytkownicy z rolą Developer/Tester/Admin W APLIKACJI mogą robić OAuth.

**Fix:** Dodaj `borsuk1916@gmail.com` jako Developer lub Tester w FB Developer Console:
→ https://developers.facebook.com/apps/937795249248975/roles/roles/

Kliknij **"Add People"** → wpisz email → rola: **Tester** → potwierdź.

## Po dodaniu do ról — OAuth URL

Piotr loguje się na FB jako `borsuk1916@gmail.com`, potem otwiera:

```
https://www.facebook.com/v20.0/dialog/oauth?client_id=937795249248975&redirect_uri=https%3A%2F%2Fklauzule.tail4676a1.ts.net%2Fmeta%2Foauth&scope=pages_manage_posts%2Cpages_show_list%2Cpages_read_engagement%2Cinstagram_basic%2Cinstagram_content_publish&response_type=code
```

Klika **"Kontynuuj"** → handler VPS automatycznie:
1. Wymienia code na long-lived token
2. Znajduje stronę Magdy w liście stron Piotra
3. Wysyła page token do magda-agent (Mac port 8000)
4. Wyświetla stronę "Gotowe!" — token aktywny

## Logi VPS (błędy 502 — nieistotne)

502 BrokenPipe w logach to proxy do OpenClaw (port 8787) gdy OpenClaw nie odpowiada — niezwiązane z OAuth, ignoruj.
