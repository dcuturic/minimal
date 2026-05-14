# Hosting Viewer

Der **Hosting Viewer** ist eine Minimal-Lösung, um Hosting-Daten strukturiert anzuzeigen und zu verarbeiten. Diese Komponente stellt eine API-Schnittstelle zur Verfügung, die von externen Systemen konsumiert werden kann.

## Externe Verwendung der API

Die Schnittstelle kann extern verwendet werden, indem ein `POST`-Request mit den erforderlichen Parametern (`source`, `config`, `mode`) als JSON-Body an den Endpoint gesendet wird.

**Endpoint:**
`POST /api/minimal-solutions/hosting_viewer`

### Request-Beispiel

```json
{
  "source": "{\"host\": \"example.com\", \"viewer_enabled\": true}",
  "config": "{\"strict\": true}",
  "mode": "quick"
}
```

### Response-Beispiel

```json
{
  "success": true,
  "data": {
    "source": "{\"host\": \"example.com\", \"viewer_enabled\": true}",
    "config": "{\"strict\": true}",
    "mode": "quick",
    "view_result": "...",
    "message": "Hosting successfully viewed."
  },
  "error": null,
  "warnings": [],
  "meta": {}
}
```
