# Kampanie Meta Ads — raport dzienny

*Ostatni update: 2026-06-17*

---

## CIEŃ Festiwal | konto: act_2241371043056679

| Ad Set | ID | Wydano PLN | Kliknięcia | CTR | CPC PLN | Reach | Freq | Status |
|--------|-----|-----------|-----------|-----|---------|-------|------|--------|
| Cien_Purchase_broad | 120243879345870450 | 740,05 | 1211 | 3,76% | 0,61 | 18 040 | 1,78 | ✅ ACTIVE |
| Reel_CzarnoCzerwone_Broad | 120247402307310450 | 806,54 | 1077 | 3,36% | 0,75 | 14 090 | **2,27** | ⚠️ ACTIVE |
| RT_Visitors14d_v1 | 120248289679970450 | 17,37 | 12 | 2,07% | 1,45 | 281 | 2,06 | ⏸️ PAUSED |

## SACRUM | konto: act_4334961180078194

| Ad Set | ID | Wydano PLN | Kliknięcia | CTR | CPC PLN | Reach | Freq | Status |
|--------|-----|-----------|-----------|-----|---------|-------|------|--------|
| AS_TOF_Animacja | 120254309425090197 | 254,24 | 389 | 4,09% | 0,65 | 6 809 | 1,40 | ✅ ACTIVE |
| AS_TOF_Specjalisci | 120254023818930197 | 344,29 | 511 | 4,04% | 0,67 | 9 473 | 1,33 | ✅ ACTIVE |

**Łączny wydatek obu kont:** 2 162 PLN / 7 dni

---

## Analiza

- **Cien_Purchase_broad** — CTR 3,76%, CPC 0,61 PLN, reach 18k, freq 1,78. Stabilna. Nie ruszaj.
- **AS_TOF_Animacja** — CTR 4,09%, CPC 0,65 PLN. Najlepsza kreacja. Zwiększ budżet.
- **AS_TOF_Specjalisci** — CTR 4,04%, CPC 0,67 PLN. Dobra, monitoruj.
- **Reel_CzarnoCzerwone_Broad** — freq 2,27, reach słaby. Zmęczenie kreacji. Rozważ nowe wideo lub wyłącz.
- **RT_Visitors14d_v1** — PAUSED ✅ (freq 2,06 na 281 osobach — słusznie wstrzymane).

## Zarządzanie kampaniami

Bot może pauzować/wznawiać ad sety:
```
python3 /root/meta-ads-request.py pause 120247402307310450 act_2241371043056679
python3 /root/meta-ads-request.py resume 120247402307310450 act_2241371043056679
```
Requestsy wykonuje Claude Code na Macu przez Supermetrics (co 30 min auto-check).

---

*Źródło: Supermetrics Meta Ads | Okres: ostatnie 7 dni*
*Następny update: 2026-06-18 06:00 (Claude Cron)*
