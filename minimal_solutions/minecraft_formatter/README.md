# Minecraft Formatter

Der **Minecraft Formatter** ist eine Minimal-Lösung, die Minecraft-Daten (NBT-ähnliche Strings) strukturiert und formatiert. 
Das Tool bietet sowohl eine UI-Demo für manuelle Tests als auch eine API-Schnittstelle für externe Integrationen.

## Externe Verwendung (API)

Die Schnittstelle kann von externen Systemen aufgerufen werden, indem ein `POST`-Request mit den entsprechenden Parametern (`input_text`, `options`, `mode`) als JSON-Body gesendet wird.

### Endpoint

`POST /api/minimal-solutions/minecraft_formatter`

### Request-Beispiel

```json
{
  "input_text": "{id:\"minecraft:stone\",Count:1b}",
  "options": {"indent": 4},
  "mode": "pretty"
}
```

### Response-Beispiel

```json
{
  "success": true,
  "data": {
    "input_text": "{id:\"minecraft:stone\",Count:1b}",
    "options": {
      "indent": 4
    },
    "mode": "pretty",
    "formatted_data": "{\n    id: \"minecraft:stone\",\n    Count: 1b\n}",
    "status": "success",
    "message": "Minecraft Daten erfolgreich formatiert."
  },
  "error": null,
  "warnings": [],
  "meta": {}
}
```
