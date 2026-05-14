# Hosting Merger

## Beschreibung
Der "Hosting Merger" führt Hosting-Daten von verschiedenen Quellen zusammen. Die Lösung steht sowohl als kleine UI-Demo als auch als API-Schnittstelle bereit.

## Externe Verwendung (API)
Die Schnittstelle kann von externen Systemen aufgerufen werden, indem ein `POST`-Request mit den entsprechenden Parametern (`source`, `config`, `mode`) als JSON-Body gesendet wird.

**Endpoint:** `POST /api/minimal-solutions/hosting_merger`  
**Content-Type:** `application/json`

### Request-Beispiel
```json
{
  "source": "[{\"domains\": [\"example.com\"]}, {\"domains\": [\"test.com\"]}]",
  "config": "{}",
  "mode": "default"
}
```

### Response-Beispiel
```json
{
  "success": true,
  "data": {
    "source": "[{\"domains\": [\"example.com\"]}, {\"domains\": [\"test.com\"]}]",
    "config": "{}",
    "mode": "default",
    "merged_data": "...",
    "message": "Hosting data successfully merged."
  },
  "error": null,
  "warnings": [],
  "meta": {}
}
```
