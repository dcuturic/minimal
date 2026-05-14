# Website Health Check Demo

Ein Tool zur Überprüfung der Erreichbarkeit und Antwortzeit einer Website.

## Verwendung
Die API kann über einen POST-Request unter `/api/minimal-solutions/website_health_check_demo` angesprochen werden. Sie eignet sich hervorragend zur Integration in externe Monitoring-Systeme oder Dashboards.

## API-Schnittstelle
- **Endpoint**: `/api/minimal-solutions/website_health_check_demo`
- **Methode**: `POST`
- **Content-Type**: `application/json`

### Request-Beispiel
```json
{
  "url": "https://example.com"
}
```

### Response-Beispiel
```json
{
  "status": "success",
  "data": {
    "url": "https://example.com",
    "is_up": true,
    "status_code": 200,
    "response_time_ms": 150,
    "checked_at": "2026-05-12T08:50:00Z"
  }
}
```
