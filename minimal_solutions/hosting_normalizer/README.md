# Hosting Normalizer

Diese Minimal-Lösung bietet eine einfache Schnittstelle zur Normalisierung von Hosting-Daten (z.B. Provider, Status, Metadaten).

## Externer Aufruf der API

Die Funktionalität wird als REST-API bereitgestellt und kann von externen Systemen aufgerufen werden.

**Endpoint:** `POST /api/minimal-solutions/hosting_normalizer`  
**Content-Type:** `application/json`

### Request-Beispiel

Ein Aufruf per `curl` oder aus einem beliebigen System erfolgt durch Übergabe eines JSON-Bodys mit den Feldern `source`, `config` und `mode`:

```bash
curl -X POST http://<host>/api/minimal-solutions/hosting_normalizer \
  -H "Content-Type: application/json" \
  -d '{
    "source": "{\"hostings\": [{\"provider\": \" AWS \", \"status\": \"active\"}, {\"provider\": \"hetzner\", \"status\": \"  INACTIVE \"}]}",
    "config": "{\"lowercase\": true}",
    "mode": "default"
  }'
```

### Response-Beispiel

Die API gibt ein strukturiertes JSON-Objekt im Standardformat der Plattform zurück:

```json
{
  "success": true,
  "data": {
    "source": "{\"hostings\": [{\"provider\": \" AWS \", \"status\": \"active\"}, {\"provider\": \"hetzner\", \"status\": \"  INACTIVE \"}]}",
    "config": "{\"lowercase\": true}",
    "mode": "default",
    "normalized_data": "...",
    "message": "Hosting data successfully normalized."
  },
  "error": null,
  "warnings": [],
  "meta": {
    "timestamp": "2026-05-14T12:00:00.000Z",
    "request_id": "req-12345"
  }
}
```

## Verwendung der UI

Für einen direkten, interaktiven Test kann die UI unter `/minimal-solutions/hosting_normalizer` aufgerufen werden. Dort steht eine Live-Vorschau und ein Formular für die Dateneingabe zur Verfügung.
