# Hosting Cleaner

Diese Minimal-Lösung bietet eine einfache Schnittstelle zur Bereinigung von Hosting-Daten (z.B. Domains, IPs).

## Externer Aufruf der API

Die Funktionalität wird als REST-API bereitgestellt und kann von externen Systemen aufgerufen werden.

**Endpoint:** `POST /api/minimal-solutions/hosting_cleaner`  
**Content-Type:** `application/json`

### Request-Beispiel

Ein Aufruf per `curl` oder aus einem beliebigen System erfolgt durch Übergabe eines JSON-Bodys mit den Feldern `source`, `config` und `mode`:

```bash
curl -X POST http://<host>/api/minimal-solutions/hosting_cleaner \
  -H "Content-Type: application/json" \
  -d '{
    "source": "{\"domains\": [\" example.com \", \"test.com\\n\", \"EXAMPLE.com\"], \"ips\": [\" 192.168.1.1\", \"10.0.0.1  \"]}",
    "config": "{\"remove_duplicates\": true}",
    "mode": "default"
  }'
```

### Response-Beispiel

Die API gibt ein strukturiertes JSON-Objekt im Standardformat der Plattform zurück:

```json
{
  "success": true,
  "data": {
    "source": "{\"domains\": [\" example.com \", \"test.com\\n\", \"EXAMPLE.com\"], \"ips\": [\" 192.168.1.1\", \"10.0.0.1  \"]}",
    "config": "{\"remove_duplicates\": true}",
    "mode": "default",
    "clean_data": "...",
    "message": "Hosting data successfully cleaned."
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

Für einen direkten, interaktiven Test kann die UI unter `/minimal-solutions/hosting_cleaner` aufgerufen werden. Dort steht eine Live-Vorschau und ein Formular für die Dateneingabe zur Verfügung.
