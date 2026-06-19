---
status: w_trakcie
priorytet: wazne
termin: 2026-06-30
utworzone: 2026-06-19
projekt: [[Zadania/projekty/Cien]]
rodzic:
---

# Zbuduj premium PWA dla uczestników CIEŃ Festiwal

## Cel

Klikalny prototyp PWA offline-first dla ~999 uczestników CIEŃ Festiwal (3–5 lipca 2026, Zamek Świny). Warstwa 1+2 gotowa do oceny przed deadline 30.06.

## Kontekst

**Architektura:** statyczna PWA, offline-first, instalowalna (manifest + service worker), zero backendu, zero kont, local-first (localStorage/IndexedDB).

**Design:** czerń/pergamin/złoto/burgund, Cinzel Bold + EB Garamond, estetyka „dark premium". Motyw nawigacji: łuk alchemiczny nigredo→albedo→rubedo.

**Deploy:** Cloudflare Pages/Netlify, subdomena `app.cienfestiwal.com` (1 rekord DNS). Dystrybucja: link + QR w PDF programu, emailu i tablicach na zamku.

**Filozofia:** narzędzie wspierające obecność, nie kradnące jej. Mniej powiadomień niż konkurencja.

## Podzadania

- [ ] Zaciągnij grafik z `program_cien_festiwal_v415.pdf` → JSON (jedno źródło prawdy)
- [ ] Warstwa 1: Harmonogram 6 stref z detekcją kolizji + widok teraz/za chwilę (zegar urządzenia)
- [ ] Warstwa 2: Interaktywna mapa stref + Lochy, klikalne POI (jadło/woda/toalety/pomoc)
- [ ] Dziennik przemiany (nigredo/albedo/rubedo, prompt dzienny, lokalny + „wyślij na maila")
- [ ] Hub redukcji szkód / Sacrum (statyczny, zawsze dostępny)
- [ ] Info praktyczne (dojazd, co zabrać, pogoda, kontakt@cienfestiwal.com)
- [ ] PWA manifest + service worker (offline cache)
- [ ] Deploy na Cloudflare Pages + DNS app.cienfestiwal.com

## Powiązania

- Projekt: [[Zadania/projekty/Cien]]

## Notatki

#### Zakresy

**v1 (warstwa 1+2) — DO 30.06:**
1. Harmonogram 6 stref: Podświadomości, Sacrum, Anima/Animus, UMBRA/Scena Główna, Kino Gnoza, Lochy
2. Mapa interaktywna + POI
3. Dziennik przemiany (lokalny)
4. Hub redukcji szkód / Sacrum
5. Info praktyczne

**Świadomie POZA v1 (faza 2 po festiwalu):**
- Push notifications (wymaga backendu, problematyczne na iOS)
- Matching Coniunctio (wymaga moderacji + danych)

#### Źródła

- Grafik: `program_cien_festiwal_v415.pdf` — zaciągnij jako JSON, NIE przepisuj ręcznie
- Kontakt ogólny: kontakt@cienfestiwal.com

---

*Utworzono: 2026-06-19*
