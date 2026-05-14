# TikTok Caption Generator

Der TikTok Caption Generator erstellt basierend auf einem Thema und einem gewünschten Tonfall (z.B. lustig, viral, edukativ) passende TikTok-Captions.
Diese Minimal-Lösung kann über die UI verwendet werden oder über die REST-API in eigene Systeme integriert werden.

## API Integration

Die Funktionalität steht als API zur Verfügung, die JSON-Anfragen verarbeitet.

### Endpunkt
`POST /api/minimal-solutions/tiktok_caption_generator`

### Request Beispiel

```json
{
  "topic": "Mein Morgen als Softwareentwickler",
  "tone": "viral"
}
```

### Response Beispiel

```json
{
  "status": "success",
  "data": {
    "captions": [
      "Wait until the end... 🤯 you won't believe this Mein Morgen als Softwareentwickler hack! ✨",
      "POV: you just found the best way to do Mein Morgen als Softwareentwickler 💯 #trending",
      "Hier ist eine viral caption über Mein Morgen als Softwareentwickler! 🔥👇 #fyp #viral"
    ]
  }
}
```
