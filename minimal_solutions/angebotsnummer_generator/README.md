# Angebotsnummer Generator

Der Angebotsnummer Generator ist eine Minimal-Lösung zur standardisierten und systematischen Generierung von Angebotsnummern. Er bietet eine einfache Web-Oberfläche sowie eine REST-API-Schnittstelle.

## Funktionen
- Generierung von Angebotsnummern nach dem Muster: `[Prefix]-[Date]-[Customer]-[Number]`
- Flexible und optionale Parameter
- REST API zur nahtlosen externen Integration

## API Schnittstelle extern verwenden

Die Lösung kann von jedem externen System (ERP, CRM, Skripte) via HTTP POST aufgerufen werden.

### Endpunkt
`POST /api/minimal-solutions/angebotsnummer_generator`

### Request (JSON)
```json
{
  "prefix": "ANG",
  "date": "2026-05",
  "customer_short": "CUST",
  "number": 1
}
```

### Response (JSON)
```json
{
  "status": "success",
  "data": {
    "numbers": [
      "ANG-2026-05-CUST-0001"
    ],
    "pattern": "ANG-2026-05-CUST-0001"
  }
}
```

### Verwendung mit cURL
```bash
curl -X POST https://deinedomain.de/api/minimal-solutions/angebotsnummer_generator \
-H "Content-Type: application/json" \
-d '{"prefix": "ANG", "date": "2026-05", "customer_short": "CUST", "number": 1}'
```
