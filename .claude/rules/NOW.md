# NOW — Bieżący kontekst

*Ostatni update: 2026-06-15 23:30*

## Aktywne projekty

| Projekt | Status | Deadline | Uwagi |
|---------|--------|----------|-------|
| Personal OS Claude Code | Gotowy | — | Pełen stack: Happy + Claude Code + Telegram Channels + Tailscale + vault-git na VPS; cloud routines aktywne |
| Marketing SACRUM | Aktywny | ciągły | Pozyskiwanie klientów terapia psychodeliczna, Meta Ads + IG |
| Matejuk AI | ✅ Live | — | OpenClaw (@matejukAI2_bot) live na VPS klauzule, Genspark/Claude Sonnet 4.6, webhook keeper aktywny; email IMAP działa (piotr@sacrum.life + piotr.matejuk@gmail.com) |
| Magda marketing | Startuje | — | Od zera: socjale, marka osobista, Google/Meta Ads, baza mailingowa |
| egoisnt.com | Aktywny | — | CRM w budowie, Shopify/Next.js |

## Priorytety tego tygodnia

1. Marketing SACRUM — pierwsze kampanie / content
2. Matejuk AI — zdefiniować zakres MVP agenta
3. Magda — uruchomić profile social media
4. Claude Cron — ✅ zainstalowany na VPS i Mac; czeka na login Claude CLI na VPS (1 krok ręczny)

## Otwarte decyzje

- [x] Obsidian Git: restrictedMode=false, plugin aktywny ✅ (jeśli nie działa — restart Obsidiana)
- [x] Claude Cron: Claude CLI zalogowany jako piotr.matejuk@gmail.com ✅
- [x] Claude Cron: 3 joby skonfigurowane (memory-update 06:00, weekly-report pon 08:00, vault-git-pull co 4h) ✅
- [x] GitHub App: zainstalowany na piotrmatejuk-noetica/asystentAI ✅

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
- 2026-06-11: Matejuk AI zbudowany — bot live 24/7 (systemd matejuk-ai-bot), Claude Cron jobs: email-morning (05:00 UTC=07:00 Warsaw) + email-check (co 2h); czeka na App Passwords
- 2026-06-11: SessionStart hook skonfigurowany — auto-uruchamia /memory-update na starcie sesji
- 2026-06-11: skill kie-generate zainstalowany — Kie.ai + ImgBB skonfigurowane, brand rules SACRUM, output Marketing/media/
- 2026-06-11: Claude Cron VPS zainstalowany — systemd claude-cron.service, port 7777, workspace /home/claude/vault-git, Claude zalogowany jako piotr.matejuk@gmail.com
- 2026-06-11: Claude Cron Mac zainstalowany — /Users/piotrmatejuk/Documents/claude-cron, autostart hook w settings.json, CLAUDE_CRON_VPS_URL=http://100.120.58.26:7777
- 2026-06-11: 3 joby skonfigurowane: memory-update (co dzień 06:00 Warsaw), weekly-report (pon 08:00 Warsaw), vault-git-pull (co 4h)
- 2026-06-10: deep-research skill działa — perplexity/sonar-deep-research przez OpenRouter, koszt ~$0.20/raport
- 2026-06-15: Matejuk AI (@matejukAI2_bot) pełna wersja live — nowy bot token (Hostinger conflict fixed), webhook-keeper aktywny, 4 pliki workspace (SOUL/TOOLS/AGENTS/MEMORY), vault-git read, email IMAP obie skrzynki, Genspark/claude-sonnet-4-6
- 2026-06-15: Email WYSYŁANIE aktywne — email-send.py SMTP, konta piotr + sacrum
- 2026-06-15: WhatsApp Bridge live — wa-bridge.service (whatsapp-web.js), sparowany z kontem Piotra, localhost:3000
- 2026-06-17: Pełna integracja bota: skrypty email-check/send, mailerlite-status/send, meta-ads-status/toggle, supermetrics-query, gdrive-read na VPS. Brakuje 3 tokenów od Piotra (META_USER_TOKEN, MAILERLITE_API_KEY, gcloud re-auth)

## Blokery

- **Meta Ads management**: potrzebny `META_USER_TOKEN` z developers.facebook.com/tools/explorer/ (ads_read + ads_management) → dodać do `/home/claude/.matejuk-ai/.env` na VPS
- **MailerLite**: potrzebny `MAILERLITE_API_KEY` z mailerlite.com → Integrations → Developer API → dodać do `.env` na VPS
- **Google Drive na VPS**: wygasł gcloud token → `gcloud auth application-default login` na Macu, potem skopiować do VPS

## Infrastruktura VPS (5.180.180.200 / klauzule)

| Komponent | Status | Uwagi |
|-----------|--------|-------|
| Claude Code | ✅ działa | .local/bin/claude |
| Happy | ✅ działa | autostart systemd |
| Telegram Channels | ✅ 24/7 | --dangerously-skip-permissions |
| Tailscale | ✅ połączony | IP 100.120.58.26 |
| Tailscale Funnel | ✅ aktywny | https://klauzule.tail4676a1.ts.net → :8787 (OpenClaw webhook) / Claude Cron na :7777 (internal) |
| vault-git | ✅ sklonowany | /root/vault-git, pull co 4h |
| Claude Cron VPS | ✅ działa | systemd claude-cron.service, port 7777, workspace: /home/claude/vault-git |
| Claude Cron Mac | ✅ działa | /Users/piotrmatejuk/Documents/claude-cron, autostart hook, VPS URL skonfigurowany |
| Claude Login (VPS) | ✅ zalogowany | piotr.matejuk@gmail.com |
| OpenClaw Telegram | ✅ live 24/7 | @matejukAI2_bot, systemd openclaw.service, webhook https://klauzule.tail4676a1.ts.net (port 8787) |
| Webhook Keeper | ✅ działa | systemd webhook-keeper.service — resetuje webhook co 5s (Hostinger konflikt) |
| WhatsApp Bridge | ✅ sparowany | systemd wa-bridge.service, localhost:3000, whatsapp-web.js, wysyłka przez curl POST /send |
