# SKILL: kampanie-report

Pobierz dane kampanii Meta Ads z Supermetrics dla obu kont (Cień Festiwal + Sacrum), przygotuj raport z analizą i propozycjami optymalizacji, wyślij na Telegram i zapisz do vault-git.

## Konta reklamowe

- **Cień Festiwal:** `act_2241371043056679`
- **Sacrum:** `act_4334961180078194`

## Kroki do wykonania

### 1. Pobierz dane (Supermetrics MCP)

Użyj `data_query` na `ds_id=FA` z parametrami:
- `ds_accounts`: oba konta
- `fields`: `campaign_name,impressions,clicks,spend,ctr,cpc,reach,frequency`
- `date_range_type`: `last_7_days`
- `compare_type`: `prev_range`
- `settings`: `{"conversion_window": "7D_CLICK", "exclude_zero_impressions": true}`
- `timezone`: `Europe/Warsaw`

Poczekaj na wyniki przez `get_async_query_results`.

### 2. Wyślij raport na Telegram

Odczytaj `TELEGRAM_BOT_TOKEN` i `TELEGRAM_CHAT_ID` ze zmiennych środowiskowych lub z `/home/claude/vault-git/.env`.

Format raportu HTML:

```
📊 <b>Kampanie Meta Ads — ostatnie 7 dni</b>
<i>Porównanie: poprzedni tydzień</i>

<b>🎪 CIEŃ Festiwal</b>
[dane per ad set z konta act_2241371043056679]

<b>🌿 SACRUM</b>
[dane per ad set z konta act_4334961180078194]

<b>💡 Propozycje:</b>
[analiza: które kampanie tracą vs zyskują, konkretne propozycje budżetowe]

sacrum.life
```

Dla każdego ad setu pokaż:
- Wydano: X PLN (zmiana %)
- Kliknięcia: X (zmiana %)
- CTR: X% (zmiana %)
- CPC: X PLN (zmiana %)

### 3. Zapisz do vault-git

Zapisz raport do pliku `Projekty/SACRUM/kampanie/daily-report.md` w formacie markdown.

Plik musi zawierać datę generowania na górze.

Następnie w katalogu `/Users/piotrmatejuk/Desktop/PiotrekMate`:
```bash
git add Projekty/SACRUM/kampanie/daily-report.md
git commit -m "kampanie: daily report $(date +%Y-%m-%d)"
git push
```

## Uwagi

- Jeśli dane nie są dostępne (brak kampanii), napisz o tym na Telegram
- Porównanie ze znakiem + to wzrost (dobrze dla kliknięć/zasięgu, źle dla CPC/spend jeśli nie rosną konwersje)
- Nie halucynuj danych — tylko to co zwróci Supermetrics
