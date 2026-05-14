# Badge Generator API

Dieses Verzeichnis enthält die Minimal-Lösung "Badge Generator".

## Externe Nutzung der Schnittstelle

Die API kann von externen Systemen aufgerufen werden, um dynamisch Badges (SVG) für Statusanzeigen (z.B. Build passing, Coverage) zu generieren.

### API-Endpunkt
**POST** `/api/minimal-solutions/badge_generator`

### Request-Beispiel
```json
{
  "label": "build",
  "value": "passing",
  "style": "flat"
}
```

### Response-Beispiel
```json
{
  "status": "success",
  "data": {
    "badge_svg": "<svg>...</svg>"
  }
}
```

Die erzeugte SVG kann direkt in Markdown oder HTML Seiten (z.B. in GitHub READMEs) eingebunden werden.
