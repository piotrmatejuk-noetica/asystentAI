---
allowed-tools: [Bash, Read, Write]
---

# Deep Research — Perplexity via OpenRouter

Przeprowadzasz dogłębny research przez Perplexity sonar-deep-research i zapisujesz raport do Zasoby/research/.

## Workflow

### 1. Załaduj config

Przeczytaj `config.md` w tym skillu.

### 2. Pobierz temat

Temat to `$ARGUMENTS`. Jeśli pusty — napisz: "Podaj temat do zbadania."

### 3. Zadaj pytania doprecyzowujące

Zadaj maksymalnie 2 pytania:

1. **Aspekt** — co konkretnie interesuje? (np. "Porównanie techniczne / Przegląd ogólny / Zastosowanie kliniczne / Dane rynkowe")
2. **Głębokość** — "Dogłębna analiza (32k tokenów) czy szybki przegląd (16k)?"

Opcjonalnie jeśli temat wymaga: filtr języka źródeł (polskie / angielskie / oba), zakres czasowy (ostatni rok / 2 lata / bez ograniczeń).

### 4. Sformułuj query po angielsku

Na podstawie tematu i odpowiedzi sformułuj precyzyjne zapytanie po angielsku. Perplexity działa lepiej po angielsku.

**Pokaż query użytkownikowi i poczekaj na potwierdzenie:**

```
Query do wysłania:
"[zapytanie po angielsku]"

Parametry: głębokość=[standard/deep] | źródła=high | timeout=5min

Wysyłam? (Enter = tak, lub popraw query)
```

### 5. Wywołaj API i parsuj odpowiedź

Perplexity zwraca JSON z literalnymi control characters (\n, \r) w wartościach stringów — łamie standardowe parsery. Użyj poniższego skryptu który naprawia JSON przed parsowaniem:

```bash
QUERY="[potwierdzone zapytanie po angielsku]"
MAX_TOKENS=[16000 lub 32000 zależnie od wyboru]

# Zapisz surową odpowiedź do pliku tymczasowego
curl -s --max-time 300 \
  https://openrouter.ai/api/v1/chat/completions \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -H "Content-Type: application/json" \
  -H "HTTP-Referer: https://sacrum.life" \
  -H "X-Title: PiotrekMate Deep Research" \
  -d "{
    \"model\": \"perplexity/sonar-deep-research\",
    \"messages\": [{\"role\": \"user\", \"content\": \"$QUERY\"}],
    \"temperature\": 0.2,
    \"max_tokens\": $MAX_TOKENS,
    \"web_search_options\": {\"search_context_size\": \"high\"}
  }" > /tmp/dr_raw.json

# Napraw JSON (control characters + nieprawidłowe escape sequences) i parsuj
python3 - << 'PYEOF'
import sys

with open('/tmp/dr_raw.json', 'rb') as f:
    raw = f.read()

# Byte-by-byte: napraw control chars i invalid escapes wewnątrz stringów JSON
fixed = bytearray()
in_string = False
escaped = False
i = 0
while i < len(raw):
    b = raw[i]
    if escaped:
        # Sprawdź czy to prawidłowy escape sequence JSON
        valid_escapes = b'"\\\/bfnrtu'
        if chr(b) not in valid_escapes:
            fixed.extend(b'\\')  # Dodaj drugi backslash
        fixed.append(b)
        escaped = False
    elif in_string:
        if b == ord('\\'):
            fixed.append(b)
            escaped = True
        elif b == ord('"'):
            fixed.append(b)
            in_string = False
        elif b < 0x20:  # Control character w stringu
            if b == 0x0a:
                fixed.extend(b'\\n')
            elif b == 0x0d:
                fixed.extend(b'\\r')
            elif b == 0x09:
                fixed.extend(b'\\t')
            else:
                fixed.extend(f'\\u{b:04x}'.encode())
        else:
            fixed.append(b)
    else:
        if b == ord('"'):
            in_string = True
        fixed.append(b)
    i += 1

import json
data = json.loads(fixed.decode('utf-8'))

# Sprawdź błąd API
if 'error' in data:
    print(f"BLAD_API: {data['error'].get('message', str(data['error']))}")
    sys.exit(1)

content = data['choices'][0]['message']['content']
citations = data.get('citations', [])
usage = data.get('usage', {})
prompt_tokens = usage.get('prompt_tokens', 0)
completion_tokens = usage.get('completion_tokens', 0)
cost = (prompt_tokens * 0.005 + completion_tokens * 0.015) / 1000

with open('/tmp/dr_content.txt', 'w') as f:
    f.write(content)

with open('/tmp/dr_meta.txt', 'w') as f:
    f.write(f"SOURCES: {len(citations)}\n")
    f.write(f"COST: ${cost:.4f}\n")
    f.write(f"TOKENS: {prompt_tokens}+{completion_tokens}\n")
    for url in citations:
        f.write(f"URL: {url}\n")

print(f"OK: koszt=${cost:.4f} tokeny={prompt_tokens}+{completion_tokens} zrodla={len(citations)}")
PYEOF
```

Po wykonaniu:
- Treść raportu: `/tmp/dr_content.txt`
- Metadane (koszt, źródła): `/tmp/dr_meta.txt`

Odczytaj oba pliki przez Read tool.

### 6. Sprawdź wynik

Jeśli wyjście zaczyna się od `BLAD_API:` → wyświetl błąd i zatrzymaj.

Koszt sonar-deep-research: ~$0.005/1k prompt tokens + $0.015/1k completion tokens.

### 7. Stwórz raport i zapisz

1. Wygeneruj TLDR (3-5 zdań po polsku) — najważniejsze wnioski z raportu
2. Nazwa pliku: `YYYY-MM-DD-[temat-kebab-case].md`
3. Zapisz do `Zasoby/research/` według szablonu z config.md
4. Treść raportu przetłumacz na polski jeśli API zwróciło po angielsku

### 8. Potwierdzenie

```
✅ Research gotowy!

📄 Plik: Zasoby/research/YYYY-MM-DD-temat.md
📊 Źródła: N
💰 Koszt: $X.XX
⏱ Czas: ~Xs

TLDR:
[3-5 zdań]
```

## Constraints

- Nie halucynuj — wyświetlaj TYLKO treść z API
- Zawsze potwierdzaj query przed wysłaniem
- Zawsze zapisuj raport — nie pytaj czy zapisać
- Cytowania obowiązkowe
- Raport po polsku, query po angielsku

ARGUMENTS: {{command-args}}
