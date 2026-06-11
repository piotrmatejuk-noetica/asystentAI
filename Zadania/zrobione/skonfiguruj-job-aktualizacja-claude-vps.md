---
status: w_trakcie
priorytet: normalne
termin:
utworzone: 2026-06-11
projekt:
rodzic: [[w_trakcie/zainstaluj-claude-cron-vps]]
---

# Skonfiguruj job: Aktualizacja folderu .claude (VPS)

## Cel

Dodać job na VPS w Claude Cron który co 4 godziny pobiera najnowszą konfigurację .claude z git — skille, hooki, ustawienia synchronizują się automatycznie z lokalnym komputerem.

## Kontekst

Obsidian Sync nie synchronizuje folderu .claude — zmiany w skilla, hookach itp. trzeba synchronizować ręcznie lub przez ten job. Job robi git pull na ścieżce /home/claude/vault-git co 4 godziny.

## Podzadania

- [ ] Otwórz dashboard Claude Cron (przełącz na VPS)
- [ ] Kliknij "Nowy job"
- [ ] Wypełnij ustawienia:
  - **Nazwa:** Aktualizacja folderu .claude
  - **Skill:** (puste — bez skilla)
  - **Kiedy:** Co kilka godzin → Co 4 godz.
  - **Prompt/argumenty:**
    ```
    Zaktualizuj vault-git repo. Wejdź do /home/claude/vault-git i zrób git pull --ff-only. Wypisz wynik (czy były zmiany i jakie pliki). Nic więcej nie rób.
    ```
  - **Timeout:** 600000 ms
  - **Maks. powtórzeń:** 1
  - **Powiadomienie Discord:** ✓
- [ ] Kliknij Zapisz
- [ ] Przetestuj klikając "Run Now"

## Powiązania

- Rodzic: [[w_trakcie/zainstaluj-claude-cron-vps]]
- Powiązane: [[w_trakcie/skonfiguruj-job-daily-memory-update]]

## Notatki

**Ważne:** Ten job działa na VPS, nie lokalnie. Wymaga że `/home/claude/vault-git` jest skonfigurowane jako git repo z remote wskazującym na GitHub.

---

*Utworzono: 2026-06-11*
