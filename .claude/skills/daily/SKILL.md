---
name: daily
description: Codzienna aktualizacja systemu zadań - archiwizacja zakończonych, regeneracja dashboardu, raport
disable-model-invocation: true
allowed-tools: ["Read", "Write", "Bash", "Edit", "Glob"]
---

# Daily — Codzienna aktualizacja systemu zadań

Wykonujesz codzienną aktualizację systemu zarządzania zadaniami w Obsidian.

**Konfiguracja:** Zobacz [config.md](config.md) dla ścieżek, słów kluczowych i ustawień.
**Szablon raportu:** Zobacz [report-template.md](report-template.md) dla formatu wyjściowego.

---

## SEKCJA 1: Archiwizacja zakończonych (AUTO)

**ŹRÓDŁO PRAWDY:** Checkbox `[x]` w dashboardzie = zadanie wykonane.

1. Przeczytaj `Zadania/to_do.md`
2. Znajdź wszystkie linie `- [x] [[w_trakcie/nazwa-pliku|`
3. Dla każdego zaznaczonego pliku:
   - Zmień `status: w_trakcie` → `status: zrobione` w frontmatter
   - Przenieś do `Zadania/zrobione/YYYY-MM/` (utwórz folder jeśli nie istnieje)
   - Zapisz nazwę do listy zarchiwizowanych

**Bez pytania o potwierdzenie** — checkbox to decyzja.

---

## SEKCJA 2.5: Wstrzykiwanie zadań cyklicznych (AUTO)

1. Przeczytaj `Zadania/cykliczne/recurring.md` (ścieżka w config.md)
2. Sparsuj tabelę markdown — wyciągnij kolumny: **Nazwa**, **Harmonogram**, **Priorytet**, **Projekt**
3. Dla każdego wiersza sprawdź czy harmonogram pasuje do **dzisiejszej daty**:
   - `co [dzień tygodnia]` → porównaj z aktualnym dniem tygodnia (poniedziałek–niedziela)
   - `co dzień` → zawsze pasuje
   - `[N]. dnia miesiąca` → porównaj N z dniem miesiąca (np. `10. dnia miesiąca` pasuje gdy dziś jest 10.)
   - `ostatni dzień miesiąca` → sprawdź czy jutro jest 1. dzień następnego miesiąca
4. Sprawdź czy zadanie **już istnieje** w dashboardzie (`to_do.md`) po nazwie — żeby nie duplikować
5. Pasujące zadania → zapisz do listy `cykliczne_dzis` (użyte w SEKCJI 4)

**Bez pytania o potwierdzenie** — harmonogram to decyzja.

---

## SEKCJA 3: Skanowanie zadań

1. Znajdź wszystkie `.md` w `Zadania/w_trakcie/`
2. Dla każdego pliku wyciągnij z frontmatter:
   - status, priorytet, termin, projekt, rodzic, nazwa (z nagłówka #)
3. Jeśli ma pole `rodzic:` → pobierz nazwę rodzica z nagłówka pliku rodzica

**Edge cases:**
- Brak pliku → pomiń sekcję
- Pusty folder → "📭 Brak zadań" + pusty dashboard
- Brak frontmatter/błędny YAML → pomiń, dodaj ostrzeżenie
- Brak nagłówka # → użyj nazwy pliku
- Rodzic nie istnieje → wyświetl bez prefixu ↳, dodaj ostrzeżenie

---

## SEKCJA 4: Regeneracja to_do.md

1. Pobierz dzisiejszą datę
2. Kategoryzuj zadania do sekcji:
   - **ZALEGŁE** — termin w przeszłości (ZAWSZE na górze!)
   - **DZISIAJ** — termin = dziś + zadania z `cykliczne_dzis` (SEKCJA 2.5)
   - **TEN TYDZIEŃ** — termin w ciągu 7 dni (nie dziś)
   - **PÓŹNIEJ** — termin > 7 dni
   - **BEZ TERMINU** — brak terminu

3. Sortuj: najpierw termin (najwcześniejszy), potem priorytet (pilne → wazne → normalne)

4. Formatuj wpisy — WSZYSTKIE jako `- [ ]` (zobacz [report-template.md](report-template.md))
   - Wpisy cykliczne: `- [ ] 🔁 Nazwa zadania — [emoji] [priorytet]`
   - Jeśli zadanie cykliczne ma Projekt: `- [ ] 🔁 Nazwa zadania — [emoji] [priorytet] — 📁 [projekt]`

5. Nadpisz `Zadania/to_do.md` z frontmatter:
   ```yaml
   ---
   ostatnia_aktualizacja: YYYY-MM-DD HH:MM
   ---
   ```

---

## SEKCJA 5: Wyświetl raport

Użyj szablonu z [report-template.md](report-template.md).

Kolejność sekcji w raporcie:
1. 📋 ZADANIA
---

## Constraints

- Po regeneracji dashboardu wszystkie zadania mają `- [ ]`
- ZAWSZE twórz folder w zrobione/ jeśli nie istnieje
- Timestamp w raporcie: DD.MM.YYYY
- Frontmatter `ostatnia_aktualizacja`: YYYY-MM-DD HH:MM
- Używaj `—` (em dash) nie `--` w nagłówkach sekcji

---

## Przepływ

```
[Start] 
   ↓
📦 Archiwizacja [x] → zrobione/
   ↓
🔁 Cykliczne (recurring.md → cykliczne_dzis)
   ↓
📋 Skan zadań w_trakcie/
   ↓
📝 Regeneracja to_do.md
   ↓
📊 RAPORT
   ↓
[Koniec]
```