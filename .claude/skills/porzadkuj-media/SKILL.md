---
name: porzadkuj-media
description: Porządkuje grafiki, wideo i PDFy w workspace - zmiana nazw, przenoszenie, raport osieroconych
disable-model-invocation: true
allowed-tools: ["Bash"]
---

# Porządkuj Media

Porządkujesz pliki mediów w workspace Obsidian (grafiki, wideo, PDFy).

## Co robi

1. **Grafiki z wpisów** → zmiana nazwy na `YYYY-MM-DD.png` (według wpisu który je używa)
2. **Wideo z wpisów** → zmiana nazwy na `YYYY-MM-DD.mp4` (według wpisu który je używa)
3. **PDFy** → przeniesienie do `Zasoby/dokumenty/` z logiem gdzie są używane
4. **Linki** → automatyczna aktualizacja we wszystkich plikach .md
5. **Raport** → osierocone pliki (nieużywane nigdzie)

## Użycie

```bash
python3 .claude/skills/porzadkuj-media/scripts/porzadkuj_media.py
```

## Skanowane lokalizacje

- Główny folder workspace (gdzie Obsidian wkleja nowe pliki)
- `Marketing/media/`

## Konwencje nazewnictwa

| Typ | Wzorzec | Przykład |
|-----|---------|----------|
| Grafika z wpisu | `YYYY-MM-DD.png` | `2026-01-06.png` |
| Wideo z wpisu | `YYYY-MM-DD.mp4` | `2026-01-06.mp4` |
| Wiele plików w jednym wpisie | `YYYY-MM-DD_1.ext` | `2026-01-06_2.png` |
| Plik bez wpisu | bez zmian | `live_1501_banner.jpg` |

## Output

```
GRAFIKI
----------------------------------------
✓ Pasted image 20260106140028.png → 2026-01-06.png
  └─ Zaktualizowano link w: 2026-01-06.md
⚠ Osierocona: live_1501_banner.jpg

WIDEO
----------------------------------------
✓ Screen Recording 2026-01-06.mp4 → 2026-01-06.mp4
  └─ Zaktualizowano link w: 2026-01-06.md

PDFy → Zasoby/dokumenty/
----------------------------------------
✓ Umowa.pdf → Zasoby/dokumenty/Umowa.pdf
  └─ Używany w: Notatki/spotkania/klient.md

PODSUMOWANIE
========================================
Grafiki ze zmienioną nazwą: X
Wideo ze zmienioną nazwą: Y
PDFy przeniesione: Z
```

## Constraints

- Osierocone pliki tylko raportuj, nie usuwaj automatycznie
- Tylko pliki z generycznymi nazwami są zmieniane (Pasted image, Screenshot, itp.)