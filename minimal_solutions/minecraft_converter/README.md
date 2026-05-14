# Minecraft Converter

Minimal solution for Minecraft Converter.

## API Usage

The Minecraft Converter API can be used by external systems to convert, translate, or migrate Minecraft data. 

**Endpoint:** `POST /api/minimal-solutions/minecraft_converter`

Send a JSON payload with `input_text` (the data to process), `mode` (e.g., 'convert', 'translate', 'migrate'), and optionally `options` (configuration parameters).

### Request Example
```json
{
  "input_text": "{id:\"minecraft:stone\"}",
  "options": {"target_version": "1.20"},
  "mode": "convert"
}
```

### Response Example
```json
{
  "success": true,
  "data": {
    "input_text": "{id:\"minecraft:stone\"}",
    "options": {
      "target_version": "1.20"
    },
    "mode": "convert",
    "converter_output": "{id:\"minecraft:stone\"}",
    "status": "success",
    "message": "Minecraft Converter erfolgreich ausgeführt."
  },
  "error": null,
  "warnings": [],
  "meta": {}
}
```
