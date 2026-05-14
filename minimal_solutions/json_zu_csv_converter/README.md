# JSON zu CSV Converter

Eine Minimal-Lösung zum Konvertieren von JSON-Daten in das CSV-Format.

## Externe Nutzung

Die Schnittstelle kann problemlos von externen Services genutzt werden, um JSON-Payloads in CSV-Dateien zu überführen. Sende einfach einen POST-Request mit den JSON-Daten als String und dem gewünschten Trennzeichen.

**Endpoint:** `POST /api/minimal-solutions/json_zu_csv_converter`

### Request Beispiel

```json
{
  "json_text": "[\n  {\n    \"name\": \"Max\",\n    \"age\": 30\n  }\n]",
  "delimiter": ","
}
```

### Response Beispiel

```json
{
  "status": "success",
  "data": {
    "csv_text": "name,age\nMax,30"
  }
}
```
