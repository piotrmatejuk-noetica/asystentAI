---
name: magda-reel
description: "Tworzenie premium Reelsów dla Magdaleny Gajdzińskiej (magdalenagajdzinska.pl). Używaj zawsze gdy pracujesz nad nowymi reelsami Magdy. Zawiera cały stack techniczny, brand rules, ścieżki plików, voice clone ID, HeyGen pipeline, dostępne assety filmowe."
metadata:
  version: 2.0.0
---

# Magda Reel — Premium Instagram Reels

## Stack techniczny

| Narzędzie | Wersja / Szczegóły |
|-----------|-------------------|
| **Remotion** | 4.0.290, TypeScript strict |
| **Projekt** | `/Users/piotrmatejuk/Desktop/Magda_Reelsy/remotion/` |
| **Output** | `out/reelN_vX.mp4` (inkrementuj X przy każdym renderze) |
| **Format** | 1080×1920 @ 30fps (9:16 Instagram Reels) |
| **Render** | `npx remotion render MagdaReel3 out/reel3_vX.mp4 --gl=angle` |
| **ElevenLabs** | Voice clone Magdy — voice_id: `7C2CH06xbdIjvEtG0uyx`, API key: `sk_c9202f7e4176144b47840b48f6763a68f863af4b5d055ba6` |
| **HeyGen** | API key: `sk_V2_hgu_kACrPsnFlsy_CtJlrBnnNSYCMJOEl3W4QtY1aD6dYeE5` |

## Brand Magdy

```
Tło główne:   #0D2D2A (ciemny teal)
Akcent:       #C4714A (terracotta)
Tekst:        #FFFFFF
Czcionka:     Montserrat (tekst główny), Syne (brand label, cyfry)
Logo:         /Users/piotrmatejuk/Desktop/Aplikacje/Magda/logo.jpg
Logo full:    /Users/piotrmatejuk/Desktop/PiotrekMate/Projekty/Magda/materialy/logo-magda-full.png
Zdjęcie twarzy Magdy: /Users/piotrmatejuk/Desktop/Sacrum/sacrum/front/public/team_gajdzinska.png (1080×1080)
Liście tło:   remotion/public/leaves_bg.jpg (przycinane z prawej krawędzi logo_magda.jpg)
```

---

## HeyGen Pipeline (talking photo — Magda twarz + głos)

### Kluczowe zasady
- **Endpoint upload:** `POST https://api.heygen.com/v3/assets` (NIE upload.heygen.com!)
- **Endpoint video:** `POST https://api.heygen.com/v3/videos`
- **Endpoint poll:** `GET https://api.heygen.com/v1/video_status.get?video_id=...`
- **Lip-sync w Remotion:** osobny `<Audio src="voice_heygen_vN.mp3">` + `OffthreadVideo muted` — NIE unmute video (Remotion wycina audio gdy scena niewidoczna)

### Payload upload audio
```python
requests.post("https://api.heygen.com/v3/assets",
    headers={"X-Api-Key": HEYGEN_KEY},
    files={"file": ("audio.mp3", f, "audio/mpeg")})
# Response: {"data": {"asset_id": "...", "url": "https://resource2.heygen.ai/audio/{id}/original.mp3"}}
```

### Payload create video (talking photo)
```python
{
    "type": "image",
    "image": {
        "type": "base64",
        "data": photo_b64,        # base64 z team_gajdzinska.png
        "media_type": "image/jpeg"  # NIE "file_type"!
    },
    "audio_url": "https://resource2.heygen.ai/audio/{asset_id}/original.mp3",
    "aspect_ratio": "9:16",
    "resolution": "1080p",
    "background": {"type": "color", "value": "#0D2D2A"}
}
```

### Extract audio z HeyGen video (dla lip-sync)
```bash
ffmpeg -y -i magda_heygen_vN.mp4 -vn -acodec libmp3lame -q:a 2 voice_heygen_vN.mp3
```

### Pełny skrypt pipeline
Wzorcowy skrypt: `/Users/piotrmatejuk/Desktop/Magda_Reelsy/gen_reel3_v6.py`
Etapy: ElevenLabs TTS → upload audio → encode photo b64 → POST /v3/videos → poll → download → ffmpeg extract audio

---

## ElevenLabs — ustawienia dla płynnej mowy

```python
{
    "model_id": "eleven_multilingual_v2",
    "voice_settings": {
        "stability": 0.82,         # wysoka = brak wypełniaczy "yyy/eee", równy rytm
        "similarity_boost": 0.85,
        "style": 0.0,              # zero = brak ekspresji AI, naturalna Magda
        "use_speaker_boost": False # False = eliminuje wypełniacze oddechowe
    }
}
```

**Skrypt TTS — zasady zapobiegające speed-up i wypełniacze:**
- Puste linie między akapitami = pauzy
- Ostatnia linia URL bez `. ` — samo `magdalenagajdzinska.pl ` (spacja na końcu)
- Nie używać wielokropków
- Myślniki (—) w środku zdania mogą powodować pauzy/wypełniacze — zastępuj przecinkami lub dziel na zdania
- Długie, wieloczłonowe zdania skracać — ElevenLabs gubi rytm na złożonych strukturach

## Workflow optymalny (0 marnowanych kredytów HeyGen)

```
1. Zatwierdź tekst (na czacie)
2. Generuj ElevenLabs TTS → otwórz audio → zatwierdź brzmienie
3. DOPIERO PO ZATWIERDZENIU → generuj HeyGen (1 kredyt, 1 strzał)
4. HeyGen generujemy JEDEN raz — nie iterujemy
```

---

## Remotion — Reel3 pattern (talking photo)

### Lip-sync pattern (KRYTYCZNE)
```tsx
{/* ZAWSZE osobny Audio — NIE unmute OffthreadVideo */}
<Audio src={staticFile("audio/voice_heygen_vN.mp3")} volume={1.5} />
<Audio src={staticFile("audio/ambient_meditation.mp3")} volume={0.07} loop />

{/* OffthreadVideo ZAWSZE muted */}
<OffthreadVideo src={staticFile("video/magda_heygen_vN.mp4")} muted
  style={{ width: "100%", height: "100%", objectFit: "cover" }} />
```

**Dlaczego:** Remotion wycina audio OffthreadVideo gdy komponent unmountowany (gdy magdaOp=0 w scenach bez Magdy). Osobny `<Audio>` gra ciągłe przez cały film.

### Tło Magdy — liście jako ramka
```tsx
{/* Baza: liście full-bleed */}
<Img src={staticFile("leaves_bg.jpg")} style={{ width:"100%", height:"100%", objectFit:"cover" }} />
{/* HeyGen video na teal tle */}
<OffthreadVideo src={staticFile("video/magda_heygen_vN.mp4")} muted
  style={{ width:"100%", height:"100%", objectFit:"cover" }} />
{/* Liście jako ramka (transparent oval w centrum) */}
<Img src={staticFile("leaves_bg.jpg")} style={{
  width:"100%", height:"100%", objectFit:"cover",
  maskImage: "radial-gradient(ellipse 54% 62% at 50% 50%, transparent 0%, transparent 32%, rgba(0,0,0,0.55) 55%, rgba(0,0,0,0.94) 78%)",
  WebkitMaskImage: "radial-gradient(ellipse 54% 62% at 50% 50%, transparent 0%, transparent 32%, rgba(0,0,0,0.55) 55%, rgba(0,0,0,0.94) 78%)",
}} />
```

### Timing — wzór dopasowania do długości audio
```
# Znana długość HeyGen video w sekundach (np. 41.9s = 1256f)
# SCENE dobierz tak, by OUTRO_START ≈ audio_duration * 30 - 150

# Formuła:
# S[n] = S[n-1] + SCENE - XF   (XF=21)
# PAIN_START = S[6] + SCENE - XF
# OUTRO_START = PAIN_START + PAIN_DUR - XF   (PAIN_DUR=150)
# D (durationInFrames) = OUTRO_START + OUTRO_DUR   (OUTRO_DUR=120)

# Przykłady:
# audio 25.9s → SCENE=135  → D=1047  (Reel3 v1-v5)
# audio 36s   → SCENE=155  → D=1187  (Reel3 v6)
# audio 41.9s → SCENE=175  → D=1327  (Reel3 v7)

# Szacowanie SCENE dla nowej długości:
# 7*SCENE + 3 = OUTRO_START ≈ (audio_frames - 150)
# SCENE ≈ (audio_frames - 153) / 7
```

---

## Assety źródłowe

### Film dokumentalny (B-roll)
- **Plik**: `/Users/piotrmatejuk/Desktop/dream_on__hipnoza_(2025_film_polski) (1080p).mp4`
- **ZAKAZ ABSOLUTNY:** Profesor Holas — żadne ujęcie pod żadnym pozorem
- **Bezpieczne ujęcia:**
  - `~1438s` — kobieta ciemna koszula, fotel ✅
  - `~1790s` — kobieta od tyłu na polu ✅
  - Przed każdym nowym: skanuj ffmpeg thumbnails, weryfikuj wzrokowo

### Grafiki AI
- `public/img_brain.png` — glowing blue brain on black, 1080×1920
- `public/img_neural.png` — cyan neural network on black, 1080×1920

### Stock video (9:16)
- `public/video/stock_headache_9x16.mp4`
- `public/video/stock_calm_9x16.mp4`

### Audio
- `public/audio/ambient_meditation.mp3` — podkład (volume 0.07)
- `public/audio/ambient_real.mp3` — Kevin MacLeod "Ouroboros"

---

## Komponenty Remotion (Reel3)

- `Grain` — SVG turbulence szum filmowy
- `Letterbox` — czarne bary 72px góra/dół
- `AccentBars` — terracotta linie animowane
- `Brand` — "MAGDALENA GAJDZINSKA" label
- `TLine` — animowany tekst (slide-up + fade)
- `ScanLine` — sweep kinematograficzny
- `EEG` — fale mózgowe SVG (sceny naukowe)
- `BigStat` — wielka cyfra (scale-in)
- `PainReliefAnim` — pain→relief wizualizacja (przed outro)
- `Outro` — logo Ken Burns shrink exit

---

## Miniatura — Canva (NIE Remotion)

- **Design ID:** `DAHNQuDLhrk`
- Nowa miniatura = nowa strona w tym samym designie
- Styl: liście full-bleed + overlay, hook biały tekst, badge terracotta, URL dół

---

---

## Post-render — dodawanie intro + QuickTime fix

### Prepend intro animacji (ffmpeg xfade)
```bash
ffmpeg -y \
  -i intro.mp4 \
  -i reel.mp4 \
  -filter_complex "
    [0:v]trim=end=2.5,scale=1536:1920,crop=1080:1920:228:0,setpts=PTS-STARTPTS[v_intro];
    [v_intro][1:v]xfade=transition=fade:duration=0.7:offset=1.8[vout];
    [1:a]adelay=1800|1800[aout]
  " \
  -map "[vout]" -map "[aout]" \
  -c:v libx264 -profile:v high -level 4.0 -pix_fmt yuv420p -movflags +faststart \
  -c:a aac -b:a 192k \
  out/reel_final.mp4
```
- `offset=1.8` = crossfade zaczyna się 0.7s przed końcem intro (2.5-0.7=1.8)
- `adelay=1800|1800` = audio reela startuje zsynchronizowane z wejściem video
- Intro 1080×1350 → scale 1536:1920 → crop do 1080:1920 (center)
- Plik intro: `/Users/piotrmatejuk/Downloads/Magda reelsy miniatury.mp4`

### QuickTime fix (zawsze przy finalnym eksporcie)
```bash
ffmpeg -y -i input.mp4 \
  -c:v libx264 -profile:v high -level 4.0 -pix_fmt yuv420p -movflags +faststart \
  -c:a aac -b:a 192k \
  output_qt.mp4
```
Remotion render domyślnie daje YUV444 lub inny profil — QuickTime tego nie gra.

---

## Gotowe reelsy

| Plik | Temat | Status |
|------|-------|--------|
| `out/reel1_v9.mp4` | Hipnoza nie jest snem — Stanford fMRI | ✅ |
| `out/reel3_v8_qt.mp4` | Hipnoza w leczeniu bólu przewlekłego — 42% + intro | ✅ |
| `out/lek_hipnoza_magda_reel_v2.mp4` | Lęk i hipnoza — ciało migdałowate, układ nerwowy + intro | ✅ |
| `out/reel5_final.mp4` | Integracja psychodeliczna — hipnoza + oddech + intro psychodeliczne | ✅ |

---

## Intro Remotion (zamiennik Canvy)

Gdy Canva nie działa → komponent `IntroN.tsx` w Remotion, format 1080×1350 @ 30fps, 150 klatek (5s).

### Psychedeliczne intro — technika (Intro5)
- **PsychOrbs** — 5 dużych SVG ellipse z `feGaussianBlur(70)` poruszających się po sin/cos; kolory: fiolet, niebieski, czerwony, magenta, granat; `opacity={0.7}` na elementach
- **AcidPlasma** — `feTurbulence fractalNoise` z animowanym `baseFrequency` (sin/cos na f) + `feColorMatrix hueRotate` animowany `values={String((f*2.2)%360)}`; alpha row: `0 0 0 0 0.5` = stała przezroczystość
- **DMTMandala** — 3 warstwy geometrii (6-fold slow CW, 8-fold fast CCW, 6-fold petals) + 8-punktowy catmull-rom blob + 8 orbujących kolorowych kul + centralne oko
- **KRYTYCZNE:** NIE używaj `mixBlendMode: "screen"` na `AbsoluteFill` — zeruje opacity do zera. Orby/plasma bez blendMode, tylko regularne stacking
- **Overlay tła:** max `rgba(0,0,0,0.55)` — ciemniejsze zabija psychodeliki
- **psycheOp:** `fi(f,4,30) * 0.65` — nigdy poniżej 0.5 końcowego mnożnika
