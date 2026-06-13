# SKILL: post-sacrum

Publikuje post na Facebook SACRUM (i Instagram jeśli dostępne IG token).

## Użycie

`/post-sacrum [treść posta]`
`/post-sacrum [treść posta] --img [url zdjecia]`

## Kroki

1. Wyciągnij treść posta z argumentów (wszystko po `/post-sacrum`)
2. Sprawdź czy w argumencie jest `--img URL` — jeśli tak, oddziel URL od treści
3. Uruchom:

```bash
cd /Users/piotrmatejuk/Desktop/PiotrekMate && python3 publish_sacrum.py "TREŚĆ POSTA"
```

lub z obrazkiem:

```bash
cd /Users/piotrmatejuk/Desktop/PiotrekMate && python3 publish_sacrum.py "TREŚĆ POSTA" --img "URL_OBRAZKA"
```

4. Powiedz czy post poszedł na FB i/lub IG, podaj link jeśli dostępny.

## Uwagi

- FB: działa bez zdjęcia (tekst)
- IG: wymaga zdjęcia (publiczne URL)
- Token FB jest ważny ~60 dni — jak wygaśnie, zgłosi błąd "Invalid OAuth access token"
- Skrypt czyta tokeny z `.env` w workspace
