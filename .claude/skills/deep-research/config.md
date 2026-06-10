# Config: Deep Research

## Ścieżki

| Element | Ścieżka |
|---------|---------|
| Wyniki | Zasoby/research/ |
| Format nazwy pliku | YYYY-MM-DD-temat.md |

## API

| Parametr | Wartość | Opis |
|----------|---------|------|
| model | perplexity/sonar-deep-research | Model Perplexity przez OpenRouter |
| endpoint | https://openrouter.ai/api/v1/chat/completions | |
| search_context_size | high | Więcej źródeł (20+) |
| max_tokens_standard | 16000 | Szybki przegląd |
| max_tokens_deep | 32000 | Dogłębna analiza |
| temperature | 0.2 | Fakty, nie kreatywność |
| timeout | 300 | 5 minut maks |

## Język zapytań

Perplexity działa lepiej po angielsku — zawsze tłumacz query na angielski przed wysłaniem.
Raport zwracaj po polsku.

## Szablon raportu wynikowego

```markdown
---
data: YYYY-MM-DD
temat: [temat po polsku]
query_en: [query wysłane do API]
model: perplexity/sonar-deep-research
koszt: $X.XX
zrodla: N
---

# [Temat]

## TLDR
[3-5 zdań — najważniejsze wnioski]

## Raport
[Pełna treść z API]

## Źródła
1. [url]
2. [url]
...

---
*Wygenerowano: YYYY-MM-DD | Koszt: $X.XX | Źródła: N*
```
