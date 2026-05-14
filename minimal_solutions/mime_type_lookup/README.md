# MIME Type Lookup

Eine Minimal-Lösung, um MIME Types anhand von Dateiendungen, Dateinamen oder umgekehrt zu ermitteln.

## Externe Verwendung (API)

Die Schnittstelle kann problemlos von externen Anwendungen (z.B. via `curl`, Fetch-API im Browser oder Backend-Services) aufgerufen werden, indem ein POST-Request mit einem JSON-Body an den Endpunkt gesendet wird.

### Endpunkt

`POST /api/minimal-solutions/mime_type_lookup`

### Request-Beispiel

```json
{
  "query": ".json"
}
```

### Response-Beispiel (Erfolg)

```json
{
  "status": "success",
  "data": {
    "results": [
      {
        "extension": ".json",
        "mime_type": "application/json",
        "description": "JSON format"
      }
    ]
  }
}
```

### Parameter
- `query` (string, required): Der Suchbegriff. Das kann eine Dateiendung (z.B. `.json`, `csv`), ein Dateiname (z.B. `document.pdf`) oder ein MIME Type (z.B. `image/png`) sein.
