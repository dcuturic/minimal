# Port Checker Demo

Eine Minimal-Lösung, um zu überprüfen, ob ein bestimmter Port auf einem angegebenen Host offen oder geschlossen ist.

## API-Nutzung

Die Schnittstelle kann extern verwendet werden, indem ein POST-Request an `/api/minimal-solutions/port_checker_demo` gesendet wird.

### Request

Sende ein JSON-Objekt mit `host` (String) und `port` (Integer).

```json
{
  "host": "google.com",
  "port": 443
}
```

### Response

Die API antwortet mit einem JSON-Objekt, das den Status des Ports (`is_open`) enthält.

```json
{
  "status": "success",
  "data": {
    "is_open": true
  }
}
```
