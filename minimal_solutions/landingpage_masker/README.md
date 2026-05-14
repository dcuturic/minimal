# Landingpage Masker

Minimal-Lösung für den Landingpage Masker.

Diese Schnittstelle kann extern als API genutzt werden, um Landingpage-Daten programmgesteuert zu maskieren.

## API-Endpunkt

**POST** `/api/minimal-solutions/landingpage_masker`

### Request-Beispiel

```json
{
  "topic": "Produkt-Launch",
  "target": "Neukunden",
  "options": "{\"anonymize\": true}"
}
```

### Response-Beispiel

```json
{
  "status": "success",
  "data": {
    "topic": "Produkt-Launch",
    "target": "Neukunden",
    "options": "{\"anonymize\": true}",
    "masker_id": "msk_123456",
    "timestamp": "2026-05-13T12:00:00Z",
    "masked": true
  }
}
```
