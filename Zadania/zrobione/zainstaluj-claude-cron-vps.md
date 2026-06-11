---
status: zrobione
priorytet: normalne
termin:
utworzone: 2026-06-11
projekt:
rodzic:
---

# Zainstaluj Claude Cron na VPS

## Cel

Uruchomić skrypt instalacyjny Claude Cron na VPS i skonfigurować go z ścieżką vault, portem oraz Discord Webhook.

## Kontekst

Główna instalacja Claude Cron na serwerze. Po prereq, uruchamiamy właściwy skrypt instalacyjny. W trakcie konfiguracji potrzebne będą: ścieżka do vault (/home/claude/vault), port 3477 (domyślny), Discord Webhook URL. Skrypt zapyta też o Tailscale Funnel dla webhooków.

## Podzadania

- [ ] Uruchom skrypt instalacyjny Claude Cron (komenda z lekcji)
- [ ] Zaloguj się do Claude na VPS (autoryzacja OAuth, skopiować link z usuniętymi nowymi liniami)
- [ ] Podaj ścieżkę vault: /home/claude/vault
- [ ] Zostaw domyślny port 3477
- [ ] Podaj Discord Webhook URL (lub pomiń)
- [ ] Ustaw timezone (Europe/Warsaw)
- [ ] Włącz Tailscale Funnel dla webhooków (Y)
- [ ] Zapisz Dashboard URL do brudnopisu

## Powiązania

- Powiązane zadania: [[w_trakcie/zainstaluj-prereq-vps-claude-cron]]
- Powiązane zadania: [[w_trakcie/zainstaluj-tailscale-vps-i-mac]]

## Notatki

**Ważne:** Po instalacji zapisz Dashboard URL — będzie potrzebny do konfiguracji lokalnej.

---

*Utworzono: 2026-06-11*
