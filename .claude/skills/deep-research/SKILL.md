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

### 5. Wywołaj API

```bash
QUERY="[potwierdzone zapytanie po angielsku]"
MAX_TOKENS=[16000 lub 32000 zależnie od wyboru]

RESPONSE=$(curl -s --max-time 300 \
  https://openrouter.ai/api/v1/chat/completions \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -H "Content-Type: application/json" \
  -H "HTTP-Referer: https://sacrum.life" \
  -H "X-Title: PiotrekMate Deep Research" \
  -d "{
    \"model\": \"perplexity/sonar-deep-research\",
    \"messages\": [{
      \"role\": \"user\",
      \"content\": \"$QUERY\"
    }],
    \"temperature\": 0.2,
    \"max_tokens\": $MAX_TOKENS,
    \"web_search_options\": {
      \"search_context_size\": \"high\"
    }
  }")

echo "$RESPONSE"
```

### 6. Parsuj odpowiedź

Z JSON wyciągnij:
- `.choices[0].message.content` — treść raportu
- `.citations` — lista URL źródeł
- `.usage.prompt_tokens` + `.usage.completion_tokens` — do obliczenia kosztu

Koszt sonar-deep-research: ~$0.005/1k prompt tokens + $0.015/1k completion tokens. Oblicz i pokaż.

Jeśli błąd → wyświetl `.error.message` i zatrzymaj.

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
