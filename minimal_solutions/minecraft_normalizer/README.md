# Minecraft Normalizer

Die Minecraft Normalizer Minimal-Lösung ermöglicht die Standardisierung und Formatierung von Minecraft-bezogenen Texten und Daten.

## Externe API Nutzung

Dieser Service kann extern als REST-API genutzt werden, um Daten zu normalisieren.

**Endpunkt**: `POST /api/minimal-solutions/minecraft_normalizer`
**Content-Type**: `application/json`

### Request-Beispiel

```json
{
  "input_text": "  Diamond Sword   (unbreakable) ",
  "mode": "lowercase",
  "options": {
    "remove_invalid": true
  }
}
```

### Response-Beispiel

```json
{
  "success": true,
  "data": {
    "normalized_text": "diamond sword (unbreakable)",
    "mode": "lowercase",
    "options": {
      "remove_invalid": true
    },
    "message": "Normalisierung erfolgreich durchgeführt."
  }
}
```
