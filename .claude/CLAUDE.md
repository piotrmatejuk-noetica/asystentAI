# CLAUDE.md

## Rules (auto-loaded)

Pliki w `.claude/rules/` ładują się automatycznie do system promptu — bez instrukcji, bez Read na starcie sesji.

| Plik | Opis | Kiedy się ładuje |
|------|------|-----------------|
| `rules/persona.md` | Profil użytkownika, styl komunikacji, wartości | Zawsze |
| `rules/soul.md` | Osobowość AI, charakter, styl myślenia | Zawsze |
| `rules/biznes.md` | Kontekst biznesowy, stack, platformy | Zawsze |
| `rules/ai-writing-patterns.md` | Anty-AI checklist — jak pisać po ludzku po polsku | Przy pracy w `Marketing/**` |
| `rules/redakcja-hipnozy-bez-czarow.md` | Głos autora + warstwa anty-AI do książki i postów | Przy pracy w `Marketing/**` |

### Kiedy pisać — obowiązkowe zasady

**Przy każdym piśmie (post, wpis, copy, kampania, email):**
Stosuj `rules/ai-writing-patterns.md` — anty-AI checklist. Piszesz jak Piotr, nie jak chatbot.

**Przy każdym piśmie dłuższym (post IG, artykuł, fragment książki, landing, mailing):**
Stosuj `rules/redakcja-hipnozy-bez-czarow.md` — głos autora ponad elegancją, warstwa anty-AI, zasada nadrzędna: vibe autora > poprawność stylistyczna.

Tryb przełączany po typie tekstu:
- **Książka / dłuższy content** → głos autora w pełnej mocy, długi myślnik i wielokropek dozwolone
- **Marketing / social / copy** → `ai-writing-patterns.md` w pełnej mocy (długi myślnik zakazany)

## Konfiguracja Claude Code (.claude/)

Folder `.claude/` zawiera konfigurację Claude Code dla tego workspace:

| Element | Zawartość |
|---------|-----------|
| `skills/` | Skille do specjalistycznych zadań (wywoływane przez /nazwa) |
| `rules/` | Pliki kontekstowe ładowane automatycznie |

### Dostępne skille (skills/)

**Workflow / Zarządzanie:**
- `daily` — codzienna aktualizacja systemu zadań (archiwizacja, regeneracja dashboardu, raport)
- `reflect` — walidacja obserwacji o użytkowniku → aktualizacja plików kontekstowych
- `utworz-zadanie` — tworzenie nowego zadania w systemie Obsidian
- `porzadkuj-media` — porządkowanie grafik, wideo i PDFów w workspace

## Opis workspace'u

Personal OS Piotra Matejuka — zarządzanie 5 projektami (SACRUM, hipnoterapia.edu.pl, egoisnt.com, cienfestiwal.com, magdalenagajdzinska.pl), zadaniami, wiedzą i marketingiem.

## Struktura katalogów

- `.claude/` — konfiguracja Claude Code
- `Zadania/` — system zarządzania zadaniami
  - `to_do.md` — główna lista zadań (dashboard)
  - `projekty/` — aktywne projekty
  - `w_trakcie/` — zadania w toku
  - `zrobione/` — ukończone zadania
  - `cykliczne/recurring.md` — zadania cykliczne
  - `.szablony/szablon-zadania.md` — szablon zadania
- `Projekty/` — foldery per projekt
  - `SACRUM/` — marketing, notatki, materiały, kampanie
  - `Hipnoterapia/` — hipnoterapia.edu.pl / PSH
  - `Egoisnt/` — streetwear, drops
  - `Cien/` — festiwal Cień, edycje
  - `Magda/` — magdalenagajdzinska.pl
- `Zasoby/` — materiały zewnętrzne
- `Marketing/` — content i social media
  - `wpisy/` — gotowe i robocze posty
  - `media/` — grafiki, wideo do publikacji
  - `pomysły.md` — backlog pomysłów
- `Notatki/` — braindumpy i spotkania
  - `spotkania/` — notatki ze spotkań
- `Baza źródeł/` — PDFy, grafiki, materiały źródłowe które AI ma znać
- `Brudnopis.md` — scratch pad, szybkie notatki

## Konwencje

- Pliki markdown w formacie Obsidian
- Checkboxy w formacie `- [ ]` / `- [x]`

### System zadań

- **Tworzenie zadań:** ZAWSZE używaj komendy `/utworz-zadanie` — nigdy nie twórz plików zadań ręcznie
- **Nazwy zadań:** kebab-case (np. `moje-nowe-zadanie.md`)
- **Podzadania:** prefiks `_` w nazwie pliku (np. `_podzadanie.md`)
- **Emoji priorytetów w dashboard:** 🔴 pilne | 🟡 wazne | 🟢 normalne

### Baza źródeł

- Wrzucaj tu PDFy, grafiki, dokumenty które chcesz żeby AI czytał jako kontekst
- Przed sesją możesz poprosić AI o przeczytanie konkretnych plików z tego folderu
