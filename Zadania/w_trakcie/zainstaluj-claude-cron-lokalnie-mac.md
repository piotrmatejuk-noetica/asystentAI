---
status: w_trakcie
priorytet: normalne
termin:
utworzone: 2026-06-11
projekt:
rodzic:
---

# Zainstaluj Claude Cron lokalnie (Mac)

## Cel

Zainstalować Claude Cron na Macu i połączyć go z instancją na VPS — lokalny klient do zarządzania harmonogramem.

## Kontekst

Po instalacji na VPS, instalujemy lokalnego klienta na Macu. Wymagania: Node.js >18, Claude Code, Tailscale (zalogowany). Skrypt pyta o IP VPS-a (samo IP bez portu — skopiować z Dashboard URL), ścieżkę workspace/vault, autostart (Y) i Discord Webhook.

## Podzadania

- [ ] Sprawdź Node.js: `node --version` (wymagane >18)
- [ ] Sprawdź Claude Code: `claude --version`
- [ ] Upewnij się że Tailscale jest zainstalowany i zalogowany
- [ ] Utwórz folder na projekt Claude Cron
- [ ] Uruchom komendy instalacyjne z lekcji (3 komendy)
- [ ] Podaj IP VPS-a (z Dashboard URL, bez portu)
- [ ] Podaj ścieżkę do vault: /Users/piotrmatejuk/Desktop/PiotrekMate
- [ ] Włącz autostart (Y)
- [ ] Załaduj zmienne środowiskowe (komenda z lekcji)
- [ ] Zweryfikuj że hook ClaudeCronAutostart pojawił się w .claude/

## Powiązania

- Powiązane zadania: [[w_trakcie/zainstaluj-tailscale-vps-i-mac]]
- Powiązane zadania: [[w_trakcie/zainstaluj-surfing-obsidian]]

## Notatki

**Uwaga:** Nie uruchamiaj serwera ręcznie. Hook autostart odpala dashboard automatycznie przy starcie sesji Claude Code.

---

*Utworzono: 2026-06-11*
