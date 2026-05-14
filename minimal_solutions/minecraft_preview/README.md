# Minecraft Preview

Minimal-Lösung für die Generierung einer Minecraft Vorschau. Die Anwendung bietet eine Benutzeroberfläche und eine REST-API-Schnittstelle.

## Externe Verwendung der API

Die Schnittstelle kann von externen Systemen (wie Webseiten, Bots oder anderen Backend-Systemen) genutzt werden.
Dazu wird ein `POST`-Request an den Endpunkt gesendet. Der Body muss als JSON formatiert sein und den entsprechenden Payload enthalten.

**Endpoint:** `POST /api/minimal-solutions/minecraft_preview`
**Content-Type:** `application/json`

### Request-Beispiel

```json
{
  "input_text": "{id:\"minecraft:stone\",Count:1b}",
  "options": {"theme": "dark"},
  "mode": "2d"
}
```

### Response-Beispiel

Die API antwortet mit dem standardisierten JSON-Format:

```json
{
  "success": true,
  "data": {
    "input_text": "{id:\"minecraft:stone\",Count:1b}",
    "options": {"theme": "dark"},
    "mode": "2d",
    "preview_url": "https://example.com/preview/minecraft_stone",
    "status": "success",
    "message": "Minecraft Vorschau erfolgreich generiert."
  },
  "error": null,
  "warnings": [],
  "meta": {}
}
```
