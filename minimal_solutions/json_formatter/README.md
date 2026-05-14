# JSON Formatter

Eine Minimal-Lösung zum Formatieren und Minifizieren von JSON-Daten. Die Anwendung bietet eine visuelle Oberfläche und eine REST-API.

## API / Schnittstelle

Dieser Service kann extern als API genutzt werden, um JSON-Strings programmgesteuert zu formatieren oder zu minifizieren.

### Endpunkt
`POST /api/minimal-solutions/json_formatter`

### Request-Beispiel
```json
{
  "json_text": "{\"key\":\"value\"}",
  "indent": 2
}
```
* `indent` kann eine Zahl (z.B. 2 oder 4 für Leerzeichen) oder 0 sein, um das JSON zu minifizieren.

### Response-Beispiel
```json
{
  "status": "success",
  "data": {
    "formatted_json": "{\n  \"key\": \"value\"\n}"
  }
}
```

## Integration in die Plattform
- **Ordner:** `minimal_solutions/json_formatter`
- **UI Route:** `/minimal-solutions/json_formatter`
- **API Endpoint:** `/api/minimal-solutions/json_formatter`
