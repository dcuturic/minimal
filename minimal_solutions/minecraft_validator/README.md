# Minecraft Validator

Minecraft Validator ist eine Minimal-Lösung zur Validierung von Minecraft-Datenformaten (wie NBT). Sie stellt sowohl eine kleine UI-Demo als auch eine API-Schnittstelle bereit.

## Externe Nutzung (API)

Die Schnittstelle kann von externen Systemen aufgerufen werden, indem ein `POST`-Request an den Endpunkt gesendet wird.

**Endpoint:** `POST /api/minimal-solutions/minecraft_validator`

Die API akzeptiert Parameter als JSON-Body und gibt ein einheitliches JSON-Format zurück.

### Request-Beispiel

```json
{
  "input_text": "{id:\"minecraft:stone\",Count:1b}",
  "options": {
    "allow_unknown": true
  },
  "mode": "strict"
}
```

### Response-Beispiel

```json
{
  "success": true,
  "data": {
    "input_text": "{id:\"minecraft:stone\",Count:1b}",
    "options": {
      "allow_unknown": true
    },
    "mode": "strict",
    "is_valid": true,
    "status": "success",
    "message": "Minecraft Daten erfolgreich validiert."
  },
  "error": null,
  "warnings": [],
  "meta": {}
}
```
