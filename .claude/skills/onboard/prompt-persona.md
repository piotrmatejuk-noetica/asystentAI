# Instrukcja generacji persona.md

Na podstawie odpowiedzi z wywiadu (kroki 2-6) wygeneruj plik w poniższej strukturze.

## Struktura pliku

```markdown
# PERSONA — [IMIĘ I NAZWISKO]

---

## 1. TOŻSAMOŚĆ

| Pole | Wartość |
|------|---------|
| Imię i nazwisko | ... |
| Firma / Projekt | ... |
| Rola | ... |
| Język komunikacji | ... |

---

## 2. TŁO ZAWODOWE

[Skąd, dokąd, co po drodze — narracyjnie, nie punktowo]

---

## 3. STYL KOMUNIKACJI

- **Formalność:** X/5 — [opis co to oznacza w praktyce]
- **Analityczność:** X/5 — [opis]
- **Preferowany format:** [jak chce dostawać info]
- **Feedback:** [bezpośredni/owinięty, styl]

---

## 4. WARTOŚCI I ZASADY

### ZAWSZE ✓
- ✓ ...

### NIGDY ✗
- ✗ ...

### Stosunek do AI/technologii
[Krótko — partner, narzędzie, mentor?]

---

## 5. PRACA NA CO DZIEŃ

### Typowy dzień
[Opis]

### Narzędzia
[Lista]

### Aktualne projekty
[Co teraz robi]

---

## 6. BLOKERY I NAPIĘCIA

[Frustracje, wady, sprzeczności — bez lukru]

---

## 7. WSKAZÓWKI DLA AI

### Jak ze mną rozmawiać
[Konkretne wskazówki wyciągnięte z wywiadu]

### Czego nie robić
[Co wkurza w AI — bez owijania]

---

## 8. MOTYWATORY

### Nakręca mnie
[Lista]

### Drenuje mnie
[Lista]

### Testy osobowości
[Wyniki jeśli podane, puste jeśli nie]

---

*Wygenerowane: [data]*
```

## Zasady generacji

1. **Cytuj słowa usera** tam gdzie to wzbogaca profil — dosłowne wyrażenia w cudzysłowie
2. **Nie wymyślaj** niczego czego user nie powiedział — zero ekstrapolacji
3. **Puste sekcje zostaw puste** — lepiej puste niż wyssane z palca
4. **Bądź konkretny** — "zorientowany na dane, myśli liczbami" > "inteligentny"
5. **Mapuj odpowiedzi na sekcje:**
   - Krok 2 (kim jesteś) → sekcja 1 + 2
   - Krok 3 (styl) → sekcja 3
   - Krok 4 (wartości) → sekcja 4 + 5
   - Krok 5 (AI + frustracje) → sekcja 4 (stosunek do AI) + sekcja 7
   - Krok 6 (motywatory) → sekcja 6 + 8
6. **Język:** pisz w języku wywiadu (jeśli user mówi po polsku → persona po polsku)
7. **Długość:** 80-200 linii — tyle ile wymaga treść, nie więcej
