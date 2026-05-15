# Minecraft Importer

This minimal solution provides a way to import Minecraft data.

## API Endpoint
`POST /api/minimal-solutions/minecraft_importer`

### Request Payload Example
```json
{
  "input_text": "Sample block data for import.",
  "mode": "schematic",
  "options": ["compress"]
}
```

### Response Example
```json
{
  "status": "success",
  "data": {
    "input_text": "Sample block data for import.",
    "mode": "schematic",
    "options": [
      "compress"
    ],
    "message": "Import erfolgreich generiert."
  }
}
```
