# Minecraft Viewer

Minimal solution for Minecraft Viewer. This application exposes an API that can be used externally.

## API Documentation

**Endpoint:** `POST /api/minimal-solutions/minecraft_viewer`

The interface can be called by external systems by sending a `POST` request with the following JSON body parameters:
- `input_text` (String): The Minecraft data or text to process.
- `options` (Object, optional): Optional settings, e.g., `{"theme": "dark"}`.
- `mode` (String, optional): Operation mode, e.g., `"view"`, `"format"`, or `"analyze"`.

### Example Request

```json
{
  "input_text": "Player1 joined the game",
  "options": {"theme": "dark"},
  "mode": "view"
}
```

### Example Response

```json
{
  "success": true,
  "data": {
    "input_text": "Player1 joined the game",
    "mode": "view",
    "options": {
      "theme": "dark"
    },
    "status": "success",
    "message": "Minecraft Viewer request successfully processed for mode 'view'.",
    "result": {
      "view_data": "Player1 joined the game",
      "formatted": true
    }
  },
  "error": null,
  "warnings": [],
  "meta": {}
}
```
