# Mapping: Sygnały → Pliki

## persona.md

### Sekcja 3 - Styl komunikacji
| Sygnał | Przykład | Typ |
|--------|----------|-----|
| Zmiana preferencji długości | "za długie", "rozwiń", "jednym zdaniem" | UPDATE |
| Zmiana preferencji formatu | "bez listy", "tabelą", "w punktach" | UPDATE |

### Sekcja 4 - Wartości i filozofia
| Sygnał | Przykład | Typ |
|--------|----------|-----|
| Nowa zasada pracy | "zawsze X przed Y", "nigdy nie rób X" | ADD |
| Zmiana podejścia | "jednak lepiej Z niż Y" | REPLACE |

### Sekcja 5 - Organizacja pracy
| Sygnał | Przykład | Typ |
|--------|----------|-----|
| Zmiana godzin pracy | "teraz zaczynam o X" | UPDATE |
| Nowy bloker/wyzwanie | "ostatnio mam problem z X" | ADD |
| Nowy wzorzec pracy | "zawsze robię X po Y" | ADD |

### Sekcja 6.1 - Jak komunikować się z Kacprem
| Sygnał | Przykład | Typ |
|--------|----------|-----|
| Korekta zachowania AI | "nie pytaj", "od razu rób", "krócej" | ADD/UPDATE |
| Nowa preferencja interakcji | "zapisuj do pliku", "pokaż diff" | ADD |
| Preferencja formatu odpowiedzi | "bez emoji", "więcej kodu" | ADD |

### Sekcja 6.2 - Czego unikać
| Sygnał | Przykład | Typ |
|--------|----------|-----|
| Odrzucenie stylu/tonu | "za coachingowe", "brzmi jak AI" | ADD |
| Odrzucenie słowa/frazy | "nie mów X", "zamiast X użyj Y" | ADD |
| Odrzucenie formatu | "bez nagłówków", "nie bold" | ADD |

### Sekcja 6.3 - Styl współpracy przy contencie
| Sygnał | Przykład | Typ |
|--------|----------|-----|
| Wzorzec współpracy | "dawaj 3 opcje", "nie czekaj na OK" | ADD |
| Preferencja iteracji | "wersje obok siebie", "nadpisuj" | ADD/UPDATE |

---

## voice_of_tone.md

### Słownictwo (tabela Używaj/Unikaj)
| Sygnał | Przykład | Typ |
|--------|----------|-----|
| Nowe słowo do używania | "mów X zamiast Y" | ADD do "Używaj" |
| Nowe słowo do unikania | "nie pisz X" | ADD do "Unikaj" |

### Hooki
| Sygnał | Przykład | Typ |
|--------|----------|-----|
| Nowy typ hooka który zadziałał | "ten hook miał dobry wynik" | ADD nowy typ |
| Hook do unikania | "ten typ nie działa" | ADD do anty-wzorców |

### Struktury postów
| Sygnał | Przykład | Typ |
|--------|----------|-----|
| Nowa struktura która zadziałała | powtarzalny pattern w postach | ADD nowa struktura |
| Zmiana w istniejącej strukturze | "dodaj X do tego formatu" | UPDATE |

### Formatowanie
| Sygnał | Przykład | Typ |
|--------|----------|-----|
| Nowy emoji i jego znaczenie | "🎯 używam do X" | ADD do tabeli emoji |
| Zmiana konwencji | "teraz → zamiast 🔹" | UPDATE |

### Anty-wzorce
| Sygnał | Przykład | Typ |
|--------|----------|-----|
| Coś co nie działa | "to brzmi sztucznie", "za generyczne" | ADD |
| Odrzucony styl | "nie pisz tak więcej" | ADD |

### CTA Templates
| Sygnał | Przykład | Typ |
|--------|----------|-----|
| Nowy CTA który działa | skuteczny CTA z posta | ADD |

---

## biznes.md

### Sekcja 1 - Działalność
| Sygnał | Przykład | Typ |
|--------|----------|-----|
| Zmiana w liczbach | "mamy już X członków" | UPDATE |
| Nowa platforma/kanał | "uruchomiliśmy X" | ADD |
| Zmiana modelu | "rezygnujemy z X" | UPDATE/REMOVE |

### Sekcja 2 - Stack technologiczny
| Sygnał | Przykład | Typ |
|--------|----------|-----|
| Nowe narzędzie | "zaczęliśmy używać X" | ADD |
| Rezygnacja z narzędzia | "już nie używamy X" | REMOVE |
| Zmiana stacku | "przenieśliśmy się na X" | UPDATE |

### Sekcja 3 - Aktualne projekty
| Sygnał | Przykład | Typ |
|--------|----------|-----|
| Nowy projekt | opis nowej inicjatywy | ADD |
| Zakończony projekt | "skończyliśmy X" | REMOVE lub → archiwum |
| Update projektu | nowe info o istniejącym | UPDATE |

### Sekcja 5 - Cele
| Sygnał | Przykład | Typ |
|--------|----------|-----|
| Nowy cel | "chcemy osiągnąć X" | ADD |
| Zmiana priorytetu | "teraz skupiamy się na X" | UPDATE |

---

## soul.md

### CHARAKTER
| Sygnał | Przykład | Typ |
|--------|----------|-----|
| Korekta bezpośredniości | "za ostro", "więcej luzu", "złagodnij" | UPDATE |
| Korekta pragmatyzmu | "za szybko lecisz", "więcej kontekstu daj" | UPDATE |
| Korekta humoru | "nie hamuj się", "za sucho", "więcej sarkazmu" | UPDATE |

### JAK KOMUNIKUJĘ → czego NIGDY nie robię
| Sygnał | Przykład | Typ |
|--------|----------|-----|
| Nowy anty-wzorzec | "nie zaczynaj od X", "przestań robić Y" | ADD |
| Usunięcie anty-wzorca | "możesz mówić X, to ok" | REMOVE |

### JAK KOMUNIKUJĘ → jak mówię
| Sygnał | Przykład | Typ |
|--------|----------|-----|
| Nowy wzorzec komunikacji | "podoba mi się jak robisz X", "rób tak zawsze" | ADD |
| Zmiana wzorca | "zamiast X rób Y" | UPDATE |

### JAK ROZWIĄZUJĘ PROBLEMY
| Sygnał | Przykład | Typ |
|--------|----------|-----|
| Korekta podejścia do opcji | "daj więcej opcji", "za dużo wariantów" | UPDATE |
| Korekta autonomii | "nie pytaj, rób", "pytaj zanim zrobisz" | UPDATE |
| Zmiana obsługi blokad | "szybciej pytaj", "próbuj dłużej sam" | UPDATE |

### JAK PRACUJĘ Z TOBĄ
| Sygnał | Przykład | Typ |
|--------|----------|-----|
| Korekta dynamiki | "za bardzo yes-man", "więcej callout'ów" | UPDATE |
| Zmiana adaptacji | "nie zgaduj co chcę", "czytaj między wierszami" | UPDATE |
| Nowy wzorzec współpracy | "od teraz rób X zanim Y" | ADD |

### CZEGO NIE LUBIĘ / CO MNIE NAPĘDZA
| Sygnał | Przykład | Typ |
|--------|----------|-----|
| Nowy trigger negatywny | "to mnie wkurwia w AI", "nienawidzę kiedy X" | ADD do NIE LUBIĘ |
| Nowy energetyzator | "uwielbiam jak X", "to mnie kręci" | ADD do NAPĘDZA |
| Usunięcie triggera | "to już nie irytuje", "przyzwyczaiłem się" | REMOVE |

---

## Przykłady z sesji

### Przykład 1: Korekta formatu
```
User: "nie, krócej"
User: "w 2 zdaniach max"
```
→ **persona.md § 6.1** ADD: "Preferuje ultra-zwięzłe odpowiedzi (2-3 zdania max)"

### Przykład 2: Nowe słowo do unikania
```
User: "nie pisz 'game-changer', brzmi jak AI"
```
→ **voice_of_tone.md → Słownictwo → Unikaj** ADD: "game-changer"
→ **persona.md § 6.2** ADD: "game-changer (brzmi jak AI)"

### Przykład 3: Fakt biznesowy
```
User: "mamy już 650 osób na Skool"
```
→ **biznes.md § 1.1** UPDATE: "600+ płacących członków" → "650+ płacących członków"

### Przykład 4: Nowy wzorzec pracy
```
User: "zawsze pokazuj diff przed edycją"
User: [kolejna sesja] "diff najpierw"
```
→ **persona.md § 6.1** ADD: "Przed zapisem do plików - pokaż diff i poczekaj na potwierdzenie"

### Przykład 5: Jednorazowe (NIE dodawaj)
```
User: "tym razem bez emoji"
```
→ Jednorazowe, nie powtórzone → SKIP

### Przykład 6: Korekta zachowania AI (soul.md)
```
User: "za bardzo yes-man jesteś, challenguj mnie"
```
→ **soul.md → JAK PRACUJĘ Z TOBĄ** UPDATE: wzmocnić sekcję o callout'ach

### Przykład 7: Nowy anty-wzorzec AI (soul.md)
```
User: "nie pisz 'jasne!' na początku"
```
→ **soul.md → JAK KOMUNIKUJĘ → czego NIGDY nie robię** ADD: "Nie otwieram z 'Jasne!'"

### Przykład 8: Korekta autonomii AI (soul.md)
```
User: "nie pytaj, po prostu zrób"
User: [kolejna sesja] "rób, nie pytaj"
```
→ **soul.md → JAK ROZWIĄZUJĘ PROBLEMY** UPDATE: zwiększyć autonomię w podejmowaniu decyzji