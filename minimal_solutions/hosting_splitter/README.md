# Hosting Splitter

Minimal-Lösung für Hosting Splitter.

## Externe Verwendung der API

Die Schnittstelle des Hosting Splitters kann von externen Systemen aufgerufen werden. 
Senden Sie dazu einfach einen `POST`-Request mit den Parametern (`source`, `config`, `mode`) als JSON-Payload an den Endpoint.

**Endpoint:** `POST /api/minimal-solutions/hosting_splitter`

### Request-Beispiel

```json
{
  "source": "{\"domains\": [\"example.com\", \"test.com\"]}",
  "config": "{}",
  "mode": "default"
}
```

### Response-Beispiel

Bei einem erfolgreichen Request antwortet die API mit dem aufgeteilten Ergebnis im `data`-Feld:

```json
{
  "success": true,
  "data": {
    "source": "{\"domains\": [\"example.com\", \"test.com\"]}",
    "config": "{}",
    "mode": "default",
    "split_data": "..."
  },
  "error": null,
  "warnings": [],
  "meta": {}
}
```
