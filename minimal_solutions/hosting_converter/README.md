# Hosting Converter

## Beschreibung
Der Hosting Converter ist ein Tool zur Umwandlung von Hosting-Daten (wie JSON, YAML, XML) für eine kleine UI-Demo.

## Externe Verwendung (API)
Die Schnittstelle kann von externen Systemen aufgerufen werden, um Datenformate zu konvertieren. Senden Sie hierzu einen `POST`-Request mit den erforderlichen Parametern (`source`, `mode` und optional `config`) als JSON-Body an den Endpunkt.

**Endpoint:** `POST /api/minimal-solutions/hosting_converter`

### Request-Beispiel

```json
{
  "source": "{\"host\": \"example.com\", \"type\": \"shared\"}",
  "config": "{}",
  "mode": "json"
}
```

### Response-Beispiel

```json
{
  "success": true,
  "data": {
    "source": "{\"host\": \"example.com\", \"type\": \"shared\"}",
    "config": "{}",
    "mode": "json",
    "converted_data": "{\n  \"host\": \"example.com\",\n  \"type\": \"shared\"\n}",
    "message": "Hosting successfully converted."
  },
  "error": null,
  "warnings": [],
  "meta": {}
}
```
