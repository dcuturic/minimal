# Minecraft Cleaner

Minimal-Lösung für Minecraft Cleaner.

## API / Externe Nutzung

Diese Minimal-Lösung bietet eine REST-API, um Minecraft-Daten basierend auf verschiedenen Modi und Optionen zu bereinigen.

### Endpunkt
`POST /api/minimal-solutions/minecraft_cleaner`

### Request-Beispiel
```json
{
  "input_text": ["dirty_steve", "dirt_block"],
  "mode": "basic",
  "options": {
    "remove_empty": true
  }
}
```

### Response-Beispiel
```json
{
  "success": true,
  "data": {
    "input_text": ["dirty_steve", "dirt_block"],
    "mode": "basic",
    "options": {
      "remove_empty": true
    },
    "message": "Clean erfolgreich durchgeführt."
  }
}
```
