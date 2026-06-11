---
status: w_trakcie
priorytet: normalne
termin:
utworzone: 2026-06-11
projekt:
rodzic:
---

# Zainstaluj i skonfiguruj Tailscale (VPS + Mac)

## Cel

Połączyć VPS i Maca w prywatną sieć przez Tailscale — wymagane do bezpiecznej komunikacji między maszynami dla Claude Cron.

## Kontekst

Claude Cron wymaga prywatnego połączenia między VPS a komputerem lokalnym. Tailscale tworzy wirtualną sieć prywatną (VPN mesh) — darmowe narzędzie. Oba urządzenia muszą być zalogowane na to samo konto Tailscale.

## Podzadania

- [ ] Zarejestruj konto na tailscale.com
- [ ] Zainstaluj Tailscale na VPS (instalator uruchamia się w trakcie skryptu Claude Cron — kliknij Y)
- [ ] Zaloguj się na VPS do Tailscale (skopiuj link z terminala → przeglądarka → Connect)
- [ ] Pobierz i zainstaluj Tailscale na Macu (brew install tailscale lub ze strony)
- [ ] Zaloguj się na Macu na to samo konto Tailscale
- [ ] Zweryfikuj połączenie (oba urządzenia widoczne w panelu Tailscale)

## Powiązania

- Powiązane zadania: [[w_trakcie/zainstaluj-claude-cron-vps]]
- Powiązane zadania: [[w_trakcie/zainstaluj-claude-cron-lokalnie-mac]]

## Notatki

[Notatki robocze, postępy, problemy, pomysły]

---

*Utworzono: 2026-06-11*
