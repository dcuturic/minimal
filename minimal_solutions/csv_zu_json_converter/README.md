# CSV zu JSON Converter

Minimal-Lösung für das Konvertieren von CSV zu JSON.

## Externe Nutzung (API)

Diese Minimal-Lösung bietet eine API-Schnittstelle, die nahtlos in externe Applikationen und Skripte eingebunden werden kann. Du kannst die Schnittstelle verwenden, um CSV-Textdaten programmatisch in strukturierte JSON-Daten umzuwandeln.

### Endpoint
`POST /api/minimal-solutions/csv_zu_json_converter`

### Request-Beispiel
```json
{
  "csv_text": "id,name\n1,Alice\n2,Bob",
  "delimiter": ",",
  "has_header": true
}
```

### Response-Beispiel
```json
{
  "status": "success",
  "data": {
    "json_data": [
      {
        "id": "1",
        "name": "Alice"
      },
      {
        "id": "2",
        "name": "Bob"
      }
    ]
  }
}
```
