# Google Drive Sync

Reads recent files from Google Drive and saves their content to vault.

## Steps
1. Use the Google Drive MCP (`mcp__claude_ai_Google_Drive__list_recent_files`) to list 20 recent files
2. For files of interest (docs, spreadsheets shared with Piotr, not very old), use `mcp__claude_ai_Google_Drive__read_file_content` to read content
3. Save summaries to `/Users/piotrmatejuk/Desktop/PiotrekMate/Notatki/gdrive-sync.md` in format:
   ```
   # Google Drive — ostatnia synchronizacja
   *Data: {date}*
   
   ## Ostatnio zmodyfikowane pliki
   - [nazwa](link) — {data modyfikacji}
   ...
   ```
4. Git commit and push the file to sync to VPS

## Usage
Run with `/gdrive-sync` or scheduled via Claude Cron
