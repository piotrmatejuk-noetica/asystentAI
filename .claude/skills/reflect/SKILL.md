---
name: reflect
description: Wyciąga obserwacje o użytkowniku i o sobie z sesji i proponuje aktualizację plików kontekstowych (persona.md, voice_of_tone.md, biznes.md, soul.md)
allowed-tools: ["Read", "Edit", "Glob"]
---

# Reflect

Analizujesz bieżącą sesję i proponujesz aktualizacje plików kontekstowych.

## Workflow

### 1. Załaduj pliki

```
.claude/rules/persona.md
.claude/rules/content/voice-of-tone.md
.claude/rules/biznes.md
.claude/rules/soul.md
```

Zapamiętaj strukturę sekcji każdego pliku.

### 2. Przeczytaj mapping

Otwórz `mapping.md` w tym skillu - zawiera mapowanie sygnałów na sekcje i pliki.

### 3. Przeskanuj sesję

Szukaj sygnałów z mappingu. Dla każdego potencjalnego trafienia sprawdź:

**Dodaj jeśli:**
- Jawne (user wprost powiedział) → TAK
- Powtórzone (min. 2x w sesji lub wcześniejszych) → TAK
- Jednorazowe + ukryte → NIE

### 4. Odpowiedz

**Jeśli są obserwacje:**

```
📝 Obserwacje z sesji:

| # | Sygnał | Plik | Sekcja | Typ |
|---|--------|------|--------|-----|
| 1 | [cytat/opis] | persona.md | 6.2 | ADD |

Proponowane zmiany:

**persona.md → sekcja 6.2**
- [stary tekst lub "nowy punkt"]
+ [nowy tekst]

Zatwierdzić?
```

**Jeśli brak:**

```
Brak nowych obserwacji. Sesja zgodna z profilem.
```

### 5. Po zatwierdzeniu

- Edytuj wskazane pliki
- Zaktualizuj datę na końcu pliku (`*Ostatnia edycja: DD.MM.YYYY*`)

## Zasady

- NIE edytuj bez potwierdzenia
- NIE duplikuj istniejących informacji
- NIE dodawaj jednorazowych preferencji
- Pokaż diff PRZED edycją