# MailerLite Sync

Reads subscriber stats and campaigns from MailerLite MCP, saves snapshot to vault so VPS bot can read it.

## Steps

1. Use MailerLite MCP tools to query:
   - Subscriber count (total + active)
   - Recent campaigns (last 5): name, status, open rate, click rate, sent count
   - Groups/segments list with subscriber counts

2. Format and save to `/Users/piotrmatejuk/Desktop/PiotrekMate/Notatki/mailerlite-sync.md`:
   ```
   # MailerLite — ostatnia synchronizacja
   *Data: {date}*

   ## Subskrybenci
   - Łącznie: {total}
   - Aktywni: {active}
   - Nieaktywni: {unsubscribed}

   ## Grupy
   | Nazwa | Subskrybenci |
   |-------|-------------|
   | ... | ... |

   ## Ostatnie kampanie (5)
   | Nazwa | Status | Wysłano | Open rate | Click rate |
   |-------|--------|---------|-----------|-----------|
   | ... | ... | ... | ... | ... |
   ```

3. Git commit and push so VPS vault syncs:
   ```
   cd /Users/piotrmatejuk/Desktop/PiotrekMate
   git add Notatki/mailerlite-sync.md
   git commit -m "mailerlite-sync: {date}"
   git push
   ```

## MCP tools to use

MailerLite MCP tools become available after user runs `/mcp` → claude.ai MailerLite.
Use whatever subscriber/campaign/group list tools are available.

## Usage

Run with `/mailerlite-sync` or scheduled via Claude Cron (daily at 07:45)
