# Kie.ai Prompting Guide

Zasady tworzenia skutecznych promptów dla Nano Banana Pro.

---

## Struktura promptu (7 elementów)

| # | Element | Słowa kluczowe (EN) |
|---|---------|---------------------|
| 1 | Style & Art Direction | photorealistic, hyper-detailed, Pixar-style, anime, watercolor, oil painting |
| 2 | Scene Description | environment, atmosphere, mood |
| 3 | Main Subject (Hero) | central object/character with specific details |
| 4 | Camera, Lens & Cinematic | focal length (35mm, 85mm), aperture (f/1.8), perspective |
| 5 | Lighting Details | soft lighting, golden hour, rim light, volumetric rays, neon glow |
| 6 | Texture, Color & Material | glossy, matte, pastel tones, metallic surfaces |
| 7 | Negative Prompts (semantic) | describe what you WANT, not what to avoid |

---

## Zasady techniczne

| Zasada | ❌ Źle | ✅ Dobrze |
|--------|--------|-----------|
| Szczegółowość | "fantasy armor" | "ornate elven plate armor, etched with silver leaf patterns" |
| Semantyczne negacje | "no cars in the scene" | "empty, deserted street with no signs of traffic" |
| Warstwowe opisy | "nice room" | "cozy coffee shop, warm wooden tones, gentle light leaks" |

**Nie przeładowuj stylu** - max 3-4 zdania dla opisu wizualnego.

---

## Słownik kamery i oświetlenia

**Perspektywa:** aerial, worm's-eye, over-the-shoulder, extreme close-up, wide shot, low angle

**Obiektyw:** 35mm (szeroki), 50mm (naturalny), 85mm (portret), shallow DOF, f/1.8, f/2.8

**Oświetlenie:** golden hour, blue hour, rim lighting, backlight, soft diffused, volumetric fog, neon glow

**Color grading:** teal & orange, noir palette, pastel diffusion, muted tones, high contrast

---

## Składnia wag

- `(sharp focus:1.3)` = wzmocnienie elementu
- `(background blur:0.8)` = osłabienie elementu

Używaj dla kluczowych cech które muszą być wyraźne.

---

## Szablon edycji (gdy są obrazki wejściowe)

```
Using the provided image of [subject], [add/remove/modify] [element].
Ensure the change [integrates with original lighting/style/composition].
Keep [specific elements] unchanged.
```

---

## Zachowanie treści tekstowych

**Zasada krytyczna:** Gdy użytkownik podaje KONKRETNE TEKSTY do umieszczenia na grafice, WSZYSTKIE muszą być zachowane DOSŁOWNIE.

| Typ contentu | Działanie |
|--------------|-----------|
| Style, efekty, kolory | Można optymalizować |
| Konkretne teksty do wyświetlenia | **ZACHOWAJ 1:1** |
| Listy z opisami | **PRZEPISZ KAŻDY ELEMENT** |

### Format dla grafik z tekstem

```
[opis stylu i kompozycji]

TEXT CONTENT TO DISPLAY:
[SECTION: Nazwa sekcji]
• Element 1: "dokładny tekst"
• Element 2: "dokładny tekst"
```

---

## Ograniczenia

- ❌ Nie wymyślaj treści których nie znasz (logo, teksty z załączników)
- ❌ Nie skracaj treści użytkownika
- ❌ Nie dodawaj elementów których użytkownik nie wymienił
- ✅ Zawsze zachowuj PEŁNĄ treść tekstową użytkownika
