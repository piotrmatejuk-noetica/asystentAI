---
status: w_trakcie
priorytet: normalne
termin:
utworzone: 2026-06-11
projekt:
rodzic: [[w_trakcie/zainstaluj-claude-cron-lokalnie-mac]]
---

# Skonfiguruj job: Daily memory update

## Cel

Dodać job w Claude Cron (lokalnie) który codziennie rano aktualizuje kontekst sesji przez skill memory-update.

## Kontekst

Job konfiguruje się w dashboardzie Claude Cron po jego instalacji. Dashboard otwiera się automatycznie po uruchomieniu sesji Claude w Obsidianie (hook autostart).

## Podzadania

- [ ] Otwórz dashboard Claude Cron (lokalnie)
- [ ] Kliknij "Nowy job"
- [ ] Wypełnij ustawienia:
  - **Nazwa:** Daily memory update
  - **Skill:** memory-update
  - **Kiedy:** Codziennie
  - **Godzina:** 06:00
  - **Prompt/argumenty:** (puste)
  - **Timeout:** 1800000 ms
  - **Maks. powtórzeń:** 1
  - **Uruchom po przebudzeniu:** ✓
  - **Powiadomienie Discord:** ✓
- [ ] Kliknij Zapisz
- [ ] Przetestuj klikając "Run Now"

## Powiązania

- Rodzic: [[w_trakcie/zainstaluj-claude-cron-lokalnie-mac]]
- Powiązane: [[w_trakcie/skonfiguruj-job-weekly-memory-update]]

## Notatki

---

*Utworzono: 2026-06-11*
