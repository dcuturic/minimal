# Image Prompt Generator

Diese Minimal-Lösung generiert Prompts für AI Image Generatoren (wie Midjourney, DALL-E) basierend auf Subject, Style, Mood und Aspect Ratio.

## Externe Verwendung (API)

Die Lösung bietet eine API, die in externe Anwendungen integriert werden kann.

**Endpoint:** `POST /api/minimal-solutions/image_prompt_generator`

### Request-Beispiel (JSON)

```json
{
  "subject": "A futuristic city with flying cars",
  "style": "Cyberpunk",
  "mood": "Dark and gloomy",
  "aspect_ratio": "16:9"
}
```

### Response-Beispiel (JSON)

```json
{
  "status": "success",
  "data": {
    "prompt": "A futuristic city with flying cars, Cyberpunk style, Dark and gloomy mood, --ar 16:9 --v 6.0"
  }
}
```
