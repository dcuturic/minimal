# YouTube Description Generator

Eine Minimal-Lösung, um aus grundlegenden Eingaben (Titel, Zusammenfassung, Links) eine strukturierte und ansprechende YouTube-Videobeschreibung zu generieren.

## Integration / API

Diese Schnittstelle kann von externen Systemen aufgerufen werden, um Videobeschreibungen automatisiert zu generieren. Du kannst die API über einen einfachen HTTP POST Request aufrufen.

### Endpunkt

`POST /api/minimal-solutions/youtube_description_generator`

### Request-Beispiel (JSON)

```json
{
  "title": "My Awesome Vlog",
  "summary": "Exploring the beautiful landscapes of New Zealand.",
  "links": "https://instagram.com/myvlog"
}
```

### Response-Beispiel (JSON)

```json
{
  "status": "success",
  "data": {
    "description": "In this video, we explore the beautiful landscapes of New Zealand.\n\nEnjoy the video!\n\nFollow me on Instagram: https://instagram.com/myvlog\n\n#MyAwesomeVlog #NewZealand"
  }
}
```
