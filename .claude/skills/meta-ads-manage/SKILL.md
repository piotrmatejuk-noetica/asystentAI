# Meta Ads Manage

Zarządza kampaniami Meta Ads przez Supermetrics MCP. Czyta requestsy z `/requests/meta-ads-*.json`, wykonuje i zapisuje wynik.

## Jak działa
Bot na VPS tworzy plik `/root/vault-git/requests/meta-ads-CMD.json` i pushuje do git.
Ten skill czyta vault, wykonuje akcję przez Supermetrics, zapisuje wynik.

## Wywołanie manualne
`/meta-ads-manage pause ADSET_ID ACCOUNT_ID` — pauza ad setu
`/meta-ads-manage resume ADSET_ID ACCOUNT_ID` — wznowienie ad setu
`/meta-ads-manage status` — odczyt statusu wszystkich aktywnych ad setów

## Format requestu z VPS (plik JSON)
```json
{
  "action": "pause|resume",
  "adset_id": "120247402307310450",
  "account_id": "act_2241371043056679",
  "requested_by": "telegram_bot",
  "timestamp": "2026-06-17T19:00:00Z"
}
```

## Konta
- act_2241371043056679 — Cień
- act_4334961180078194 — SACRUM

## Narzędzia
Używaj `mcp__claude_ai_Supermetrics_Marketing_Analytics__campaign_update` z parametrem `ad_groups: [{id: ADSET_ID, platform_settings: {status: "PAUSED"|"ACTIVE"}}]`

## Po wykonaniu
1. Usuń plik requestu z `/requests/`
2. Zapisz wynik do `/requests/meta-ads-results.md`
3. Git commit + push żeby VPS mógł odczytać wynik
