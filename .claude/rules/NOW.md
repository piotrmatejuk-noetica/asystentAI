# NOW — Bieżący kontekst

*Ostatni update: 2026-06-11 12:00*

## Aktywne projekty

| Projekt | Status | Deadline | Uwagi |
|---------|--------|----------|-------|
| Personal OS Claude Code | Gotowy | — | Pełen stack: Happy + Claude Code + Telegram Channels na VPS; autostart; Obsidian Git czeka na Restricted Mode |
| Marketing SACRUM | Aktywny | ciągły | Pozyskiwanie klientów terapia psychodeliczna, Meta Ads + IG |
| Matejuk AI | Planowanie | — | Agent: odpowiada za Piotra na zapytania + wykonuje zadania autonomicznie |
| Magda marketing | Startuje | — | Od zera: socjale, marka osobista, Google/Meta Ads, baza mailingowa |
| egoisnt.com | Aktywny | — | CRM w budowie, Shopify/Next.js |

## Priorytety tego tygodnia

1. Marketing SACRUM — pierwsze kampanie / content
2. Matejuk AI — zdefiniować zakres MVP agenta
3. Magda — uruchomić profile social media
4. Obsidian Git — aktywować (plugin zainstalowany, Restricted Mode do wyłączenia ręcznie)

## Otwarte decyzje

- [ ] Obsidian Git: wyłączyć Restricted Mode → plugin załaduje się automatycznie (już zainstalowany + skonfigurowany)

## Ostatnie ustalenia

- 2026-06-11: Telegram Channels live — bot sparowany z ID 1763598560, policy allowlist, działa 24/7 na VPS
- 2026-06-11: Happy 1.1.8 + Claude Code 2.1.172 + Bun na VPS; autostart systemd; working dir: piotrmatejuk-noetica/asystentAI
- 2026-06-11: Obsidian Git 2.38.3 zainstalowany ręcznie w .obsidian/plugins/; auto-sync co 10 min, GitHub token skonfigurowany
- 2026-06-11: SessionStart hook skonfigurowany w .claude/settings.json — auto-uruchamia /memory-update na starcie sesji gdy są nowe logi (asyncRewake)
- 2026-06-11: Zainstalowano skill memory-update — parsuje sesje, aktualizuje NOW.md automatycznie
- 2026-06-10: deep-research skill działa — perplexity/sonar-deep-research przez OpenRouter, koszt ~$0.20/raport

## Blokery

- Obsidian Git: plugin zainstalowany ale Restricted Mode blokuje ładowanie. Fix: Obsidian → Settings → Community plugins → wyłącz "Restricted mode" → gotowe (nie trzeba nic pobierać)
- Happy first-run auth: wymaga jednorazowego `tmux attach -t claude-happy` na VPS i zeskanowania QR kodem w appce Happy
