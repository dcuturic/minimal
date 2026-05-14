# Minecraft Builder

Minecraft Builder baut Minecraft-Daten als kleine UI-Demo und stellt dieselbe Funktion als API-Schnittstelle bereit.

## API Endpunkt

**Endpoint:** `POST /api/minimal-solutions/minecraft_builder`

Die Schnittstelle kann von externen Systemen aufgerufen werden, indem ein HTTP `POST`-Request mit den entsprechenden Parametern (`input_text`, `options`, `mode`) als JSON-Body gesendet wird.

### Request-Beispiel

```json
{
  "input_text": "stone_brick_house",
  "options": {
    "version": "1.20"
  },
  "mode": "build"
}
```

### Response-Beispiel

```json
{
  "success": true,
  "data": {
    "input_text": "stone_brick_house",
    "options": {
      "version": "1.20"
    },
    "mode": "build",
    "builder_output": "...",
    "status": "success",
    "message": "Minecraft Builder erfolgreich ausgefuehrt."
  },
  "error": null,
  "warnings": [],
  "meta": {}
}
```

## Externe Verwendung

Die REST-API kann von anderen Microservices, Frontends oder Skripten genutzt werden. Es reicht aus, einen standardmäßigen HTTP `POST` Request an den Endpunkt zu senden. Als `Content-Type` Header muss `application/json` angegeben werden.
