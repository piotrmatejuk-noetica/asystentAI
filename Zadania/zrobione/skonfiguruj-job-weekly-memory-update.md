---
status: w_trakcie
priorytet: normalne
termin:
utworzone: 2026-06-11
projekt:
rodzic: [[w_trakcie/zainstaluj-claude-cron-lokalnie-mac]]
---

# Skonfiguruj job: Weekly memory update

## Cel

Dodać job w Claude Cron (lokalnie) który co poniedziałek robi tygodniowy przegląd i aktualizację kontekstu.

## Kontekst

Tygodniowa wersja memory-update z argumentem "weekly" — głębszy przegląd niż dzienny. Konfiguruje się tak samo jak daily, ale z innym harmonogramem i dodatkowym argumentem.

## Podzadania

- [ ] Otwórz dashboard Claude Cron (lokalnie)
- [ ] Kliknij "Nowy job"
- [ ] Wypełnij ustawienia:
  - **Nazwa:** Weekly memory update
  - **Skill:** memory-update
  - **Kiedy:** Raz w tygodniu
  - **Dzień:** Poniedziałek
  - **Godzina:** 08:00
  - **Prompt/argumenty:** `weekly`
  - **Timeout:** 600000 ms
  - **Maks. powtórzeń:** 1
  - **Uruchom po przebudzeniu:** ✓
  - **Powiadomienie Discord:** ✓
- [ ] Kliknij Zapisz
- [ ] Przetestuj klikając "Run Now"

## Powiązania

- Rodzic: [[w_trakcie/zainstaluj-claude-cron-lokalnie-mac]]
- Powiązane: [[w_trakcie/skonfiguruj-job-daily-memory-update]]

## Notatki

---

*Utworzono: 2026-06-11*
