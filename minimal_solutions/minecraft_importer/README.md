# Minecraft Importer

Minecraft Importer ist eine Minimal-Lösung, um Minecraft-Daten (wie Mod-Listen, World-Daten oder Log-Text) in das System zu importieren.
Diese Schnittstelle kann von externen Systemen angesprochen werden, um Importvorgänge automatisiert durchzuführen.

## Externe Verwendung

Die Schnittstelle kann von externen Systemen aufgerufen werden, indem ein `POST`-Request mit den entsprechenden Parametern (`input_text`, `options`, `mode`) als JSON-Body gesendet wird.

**API Endpoint:**
`POST /api/minimal-solutions/minecraft_importer`

### Request-Beispiel

```json
{
  "input_text": "World Data Block...",
  "options": {
    "overwrite": true
  },
  "mode": "import"
}
```

### Response-Beispiel

```json
{
  "success": true,
  "data": {
    "input_text": "World Data Block...",
    "mode": "import",
    "options": {
      "overwrite": true
    },
    "message": "Import erfolgreich generiert."
  },
  "error": null,
  "warnings": [],
  "meta": {}
}
```
