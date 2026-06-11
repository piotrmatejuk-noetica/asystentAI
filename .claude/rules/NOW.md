# NOW — Bieżący kontekst

*Ostatni update: 2026-06-11 09:30*

## Aktywne projekty

| Projekt | Status | Deadline | Uwagi |
|---------|--------|----------|-------|
| Personal OS Claude Code | Gotowy | — | Pełen stack: Happy + Claude Code + Telegram Channels + Tailscale + vault-git na VPS; cloud routines aktywne |
| Marketing SACRUM | Aktywny | ciągły | Pozyskiwanie klientów terapia psychodeliczna, Meta Ads + IG |
| Matejuk AI | Planowanie | — | Agent: odpowiada za Piotra na zapytania + wykonuje zadania autonomicznie |
| Magda marketing | Startuje | — | Od zera: socjale, marka osobista, Google/Meta Ads, baza mailingowa |
| egoisnt.com | Aktywny | — | CRM w budowie, Shopify/Next.js |

## Priorytety tego tygodnia

1. Marketing SACRUM — pierwsze kampanie / content
2. Matejuk AI — zdefiniować zakres MVP agenta
3. Magda — uruchomić profile social media
4. Claude Cron — zainstalować (czeka na komendy prereq + install z kursu)

## Otwarte decyzje

- [ ] Obsidian Git: wyłączyć Restricted Mode → plugin załaduje się automatycznie
- [ ] Claude Cron: wkleić komendy prereq + install z kursu → reszta zautomatyzowana
- [ ] GitHub App: zainstalować na repo piotrmatejuk-noetica/asystentAI (strona otwarta w przeglądarce)

## Ostatnie ustalenia

- 2026-06-11: Tailscale VPS (klauzule) połączony — IP 100.120.58.26, Funnel aktywny na https://klauzule.tail4676a1.ts.net (port 3477)
- 2026-06-11: Tailscale.app zainstalowany na Macu; SSH config: vps-klauzule → 100.120.58.26
- 2026-06-11: vault-git sklonowany na VPS → /root/vault-git; system cron git pull co 4h
- 2026-06-11: Cloud routines aktywne: memory-update (codziennie 6:00) + weekly-report (poniedziałek 8:00)
- 2026-06-11: Local launchd: vault-commit codziennie 23:00
- 2026-06-11: Surfing plugin zainstalowany w Obsidianie (przeładuj Obsidian żeby załadował)
- 2026-06-11: Telegram Channels live — bot sparowany z ID 1763598560, policy allowlist, działa 24/7 na VPS
- 2026-06-11: Happy 1.1.8 + Claude Code 2.1.172 + Bun na VPS; autostart systemd
- 2026-06-11: Obsidian Git 2.38.3 zainstalowany ręcznie; auto-sync co 10 min, GitHub token skonfigurowany
- 2026-06-11: SessionStart hook skonfigurowany — auto-uruchamia /memory-update na starcie sesji
- 2026-06-10: deep-research skill działa — perplexity/sonar-deep-research przez OpenRouter, koszt ~$0.20/raport

## Blokery

- Claude Cron: komendy prereq + install są za paywallem kursu — wklej je do chatu, reszta automatyczna
- Obsidian Git: Restricted Mode blokuje plugin. Fix: Settings → Community plugins → wyłącz "Restricted mode"
- GitHub App: wymaga kliknięcia na https://github.com/apps/claude → Install → wybrać repo asystentAI

## Infrastruktura VPS (5.180.180.200 / klauzule)

| Komponent | Status | Uwagi |
|-----------|--------|-------|
| Claude Code | ✅ działa | .local/bin/claude |
| Happy | ✅ działa | autostart systemd |
| Telegram Channels | ✅ 24/7 | --dangerously-skip-permissions |
| Tailscale | ✅ połączony | IP 100.120.58.26 |
| Tailscale Funnel | ✅ aktywny | https://klauzule.tail4676a1.ts.net → :3477 |
| vault-git | ✅ sklonowany | /root/vault-git, pull co 4h |
| Claude Cron | ⏳ czeka | komendy z kursu potrzebne |
