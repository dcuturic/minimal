# Timestamp Converter API

Der **Timestamp Converter** konvertiert Unix-Timestamps in menschenlesbare Daten (ISO-8601 ähnlich) und umgekehrt.

## Externe Nutzung

Die Schnittstelle kann extern in anderen Anwendungen genutzt werden, um Zeiten oder Timestamps programmgesteuert umzuwandeln.

**Endpoint:**
`POST /api/minimal-solutions/timestamp_converter`

**Request:**
Sende ein JSON mit den Feldern `value` (der Wert als String), `mode` ("timestamp_to_date" oder "date_to_timestamp") und `timezone` ("UTC" oder "Local").

**Beispiel-Request:**
```json
{
  "value": "1704067200",
  "mode": "timestamp_to_date",
  "timezone": "UTC"
}
```

**Beispiel-Response:**
```json
{
  "status": "success",
  "data": {
    "result": "2024-01-01 00:00:00"
  }
}
```
