# Hosting Diff Viewer

Der **Hosting Diff Viewer** ist eine Minimal-Lösung, die es ermöglicht, Unterschiede (Diffs) zwischen zwei Hosting-Konfigurationen zu berechnen und übersichtlich darzustellen.

## Externe Verwendung der API

Die Funktionalität steht über eine HTTP-API bereit und kann von externen Systemen konsumiert werden. Senden Sie dazu einen `POST`-Request mit einem JSON-Body an den unten genannten Endpoint.

**Endpoint:** `POST /api/minimal-solutions/hosting_diff_viewer`

### Parameter
- `source` (String/JSON): Die zu vergleichenden Daten, typischerweise mit `old_hosting` und `new_hosting` Objekten.
- `config` (String/JSON, Optional): Optionale Konfigurationsparameter, wie z.B. ignorierte Felder.
- `mode` (String, Optional): Verarbeitungsmodus (z.B. `default`).

### Request-Beispiel

```json
{
  "source": "{\"old_hosting\": {\"provider\": \"aws\", \"domain\": \"example.com\"}, \"new_hosting\": {\"provider\": \"gcp\", \"domain\": \"example.com\"}}",
  "config": "{\"ignore_fields\": [\"id\"]}",
  "mode": "default"
}
```

### Response-Beispiel

```json
{
  "success": true,
  "data": {
    "source": "{\"old_hosting\": {\"provider\": \"aws\", \"domain\": \"example.com\"}, \"new_hosting\": {\"provider\": \"gcp\", \"domain\": \"example.com\"}}",
    "config": {"ignore_fields": ["id"]},
    "mode": "default",
    "diff": [
      {"field": "provider", "old": "aws", "new": "gcp"}
    ],
    "status": "success",
    "message": "Diff erfolgreich berechnet."
  },
  "error": null,
  "warnings": [],
  "meta": {}
}
```
