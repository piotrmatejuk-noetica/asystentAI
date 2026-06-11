# Onboarding — kie-generate

Instrukcja dla Claude'a: jak przeprowadzić nowego użytkownika przez konfigurację skilla `kie-generate` na jego systemie (Mac/Windows/Linux).

**Wywołanie:** user mówi "skonfiguruj kie-generate" / "onboarding kie-generate" / "uruchom kie-generate setup" / "zrób mi setup kie-generate".

## Zasady działania

1. **Idempotentność** — za każdym uruchomieniem sprawdzaj stan na żywo. Jak krok już zrobiony → ✅ skip i komunikat "już skonfigurowane". Nic nie pamiętamy między sesjami.
2. **Bez realnych call testowych** — nie palimy kasy usera na weryfikację kluczy. Pytamy "dodałeś?" i sprawdzamy tylko że klucz jest w `.env`.
3. **Skip zamiast nadpisywać** — jeśli user ma już skonfigurowany brand / lokalizację outputu, nie dotykamy.
4. **Komunikacja krótka, konkretna** — każdy krok: co sprawdzam → wynik → co dalej. Bez wstępów.

## Kroki

### 1. Python 3

**Check:**
```bash
python3 --version
```

- Jeśli wersja ≥ 3.8 → ✅ "Python OK: {wersja}"
- Jeśli brak `python3` lub starsza → poinformuj usera:
  - **Mac:** `brew install python3`
  - **Windows:** pobierz z python.org, zaznacz "Add to PATH" przy instalacji
  - **Linux:** `sudo apt install python3` (Debian/Ubuntu) lub odpowiednik
- Po instalacji user musi **restartnąć terminal**, potem re-run onboardingu

### 2. Biblioteka `requests`

**Check:**
```bash
python3 -c "import requests; print(requests.__version__)"
```

- Jeśli działa → ✅ "requests OK: {wersja}"
- Jeśli `ModuleNotFoundError` → zapytaj usera: "Zainstalować `requests`? [tak/nie]"
  - Jeśli tak → `pip3 install requests` (lub `pip install requests` jeśli pip3 nie istnieje)
  - Jeśli nie → stop, poinformuj że skill nie zadziała bez tej biblioteki

### 3. Plik `.env` w workspace

**Zasada:** Claude **nie tworzy** i **nie edytuje** pliku `.env`. User sam robi to w swoim edytorze. My tylko checkujemy przez `grep` czy klucze są wypełnione.

**Check:**
```bash
test -f .env && echo "EXISTS" || echo "MISSING"
```

- Jeśli istnieje → ✅ "Plik .env znaleziony"
- Jeśli nie istnieje → **nie twórz pliku samodzielnie**. Poproś usera.

### 4. `KIE_API_KEY`

**Check:** (sprawdza czy linia istnieje I ma niepustą wartość po `=`)
```bash
grep -qE "^KIE_API_KEY=.+" .env && echo "SET" || echo "MISSING"
```

- Jeśli SET → ✅ "KIE_API_KEY w .env — skip"
- Jeśli MISSING → wyświetl userowi instrukcję z kie.ai

### 5. `IMGBB_API_KEY`

**Check:**
```bash
grep -qE "^IMGBB_API_KEY=.+" .env && echo "SET" || echo "MISSING"
```

- Jeśli SET → ✅ "IMGBB_API_KEY w .env — skip"
- Jeśli MISSING → wyświetl userowi instrukcję z imgbb.com/api

### 6. Brand rules

**Check:**
```bash
test -f .claude/skills/kie-generate/brand-rules.md && head -1 .claude/skills/kie-generate/brand-rules.md
```

- Zapytaj usera czy chce skonfigurować własny brand
- Jeśli tak — przeprowadź dialog brandowy (nazwa, kolory, styl, zastosowanie, logo URL, czego unikać)
- Wygeneruj brand-rules.md i pokaż draft przed zapisem

### 7. Lokalizacja outputu

Domyślnie `Marketing/media/` — zapytaj czy zmienić.

### 8. Podsumowanie

Wyświetl finalny status z wszystkimi skonfigurowanymi elementami.
