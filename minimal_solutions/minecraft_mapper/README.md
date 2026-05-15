# Minecraft Mapper

Diese Minimal-Lösung bietet Minecraft-Mapping-Funktionalitäten.

## Externe Nutzung der API

Die Schnittstelle kann über HTTP `POST`-Requests von beliebigen externen Anwendungen angesprochen werden, um Minecraft-Eingabedaten basierend auf einem ausgewählten Modus und weiteren Optionen (im JSON-Format) zu mappen. 

**Endpunkt:**
`POST /api/minimal-solutions/minecraft_mapper`

**Header:**
`Content-Type: application/json`

### Request-Beispiel

```json
{
  "input_text": "Diamond Sword",
  "mode": "map",
  "options": {
    "map_properties": true
  }
}
```

### Response-Beispiel

```json
{
  "success": true,
  "data": {
    "mapped_text": "Diamond Sword",
    "mode": "map",
    "options": {
      "map_properties": true
    },
    "message": "Mapping erfolgreich durchgeführt."
  }
}
```
