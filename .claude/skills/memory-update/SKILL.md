---
name: memory-update
description: Parsuje logi sesji Claude Code, wyciąga kluczowe sygnały (projekty, decyzje, priorytety, blokery) i aktualizuje NOW.md z bieżącym kontekstem pracy
allowed-tools: ["Read", "Edit", "Write", "Bash", "Glob", "Grep"]
---

# Memory Update

Skanuje logi sesji Claude Code, wyciąga sygnały i aktualizuje `.claude/rules/NOW.md` — plik ładowany automatycznie do każdej sesji.

---

## Workflow

### 1. Ustal zakres czasowy

Przeczytaj `.claude/rules/NOW.md` — weź timestamp z `*Ostatni update: YYYY-MM-DD HH:MM*`.

- **Jeśli jest timestamp:** parsuj sesje `--since "{timestamp}"`
- **Jeśli brak lub pierwszy raz:** parsuj `--days 3` (catchup mode)

### 2. Parsuj logi sesji

```bash
python3 .claude/skills/memory-update/scripts/parse_sessions.py --since "{timestamp}" 2>/tmp/mu-stats.txt > /tmp/mu-dialog.txt
```

Lub catchup:
```bash
python3 .claude/skills/memory-update/scripts/parse_sessions.py --days 3 2>/tmp/mu-stats.txt > /tmp/mu-dialog.txt
```

Sprawdź statystyki:
```bash
cat /tmp/mu-stats.txt
```

Jeśli 0 sesji → powiedz "Brak nowych sesji do przeanalizowania" i zakończ.

### 3. Ekstrakcja sygnałów

Wczytaj prompt ekstrakcji:
```
.claude/skills/memory-update/prompts/extract.md
```

Wczytaj dialog z parsera:
```bash
cat /tmp/mu-dialog.txt
```

**WAŻNE:** Jeśli dialog jest bardzo długi (>50K znaków), przetwarzaj w kawałkach — sesja po sesji.

Przeanalizuj dialog zgodnie z promptem ekstrakcji. Wygeneruj listę sygnałów JSON.

### 4. Merge do NOW.md

Wczytaj:
- Aktualny `.claude/rules/NOW.md`
- Prompt merge: `.claude/skills/memory-update/prompts/merge.md`
- Sygnały z kroku 3

Wygeneruj zaktualizowany NOW.md zgodnie z zasadami merge. Zaktualizuj timestamp na bieżący.

### 5. Zapisz NOW.md

Zapisz zaktualizowany plik do `.claude/rules/NOW.md`.

### 6. Wyświetl podsumowanie

Pokaż:

```
🧠 Memory Update | {data}

Sesje: {N} | Wiadomości usera: {N}

DODANE:
+ [kategoria] opis

ZAKTUALIZOWANE:
~ [kategoria] opis

USUNIĘTE:
- [kategoria] opis (powód)
```

## Zasady

- NOW.md max **120 linii**
- **NIE duplikuj** info z innych plików w `.claude/rules/` ładowanych do kontekstu
- **NIE interpretuj emocji** usera — tylko fakty i explicite statements
- Confidence **LOW → odrzuć** (nie zapisuj)
- Stale data → usuń automatycznie (reguły w merge prompt)
- Full auto — **nie pytaj o zatwierdzenie**, po prostu zapisz
- Cleanup: po zapisie usuń pliki tymczasowe (`/tmp/mu-*.txt`)
