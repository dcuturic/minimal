# Minecraft Generator

Minimal-Lösung "Minecraft Generator" erstellt Minecraft-Daten und stellt diese als API-Schnittstelle zur Verfügung.

## Verwendung (Extern)

Die Schnittstelle kann von externen Systemen genutzt werden.

### API Endpoint

`POST /api/minimal-solutions/minecraft_generator`

### Request-Beispiel

```json
{
  "input_text": "Diamond Sword",
  "options": {
    "version": "1.20"
  },
  "mode": "default"
}
```

### Response-Beispiel

```json
{
  "success": true,
  "data": {
    "input_text": "Diamond Sword",
    "options": {
      "version": "1.20"
    },
    "mode": "default",
    "generated_data": {
      "item": "minecraft:diamond_sword",
      "count": 1
    },
    "status": "success",
    "message": "Minecraft Daten erfolgreich generiert."
  },
  "error": null,
  "warnings": [],
  "meta": {}
}
```

## UI

Eine einfache UI-Demo zur Interaktion ist unter `/minimal-solutions/minecraft_generator` verfügbar.
