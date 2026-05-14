# Hosting Importer

Dieses Tool dient als Minimal-Lösung, um Hosting-Daten zu importieren. Es verfügt über eine UI-Demo sowie eine eigenständige API, die von externen Systemen aufgerufen werden kann.

## API-Nutzung

Die Funktionalität des Hosting Importers ist über einen API-Endpunkt erreichbar. Externe Systeme können diese Schnittstelle nutzen, indem sie strukturierte JSON-Daten per `POST`-Request senden.

### Endpunkt
`POST /api/minimal-solutions/hosting_importer`

### Request-Parameter

- **source** (string, Pflichtfeld): Die zu importierenden Daten als JSON-String. Enthält typischerweise Informationen über den Host und die Import-Daten (z. B. `{"host": "example.com", "import_data": {}}`).
- **config** (string, optional): Zusätzliche Konfigurationen als JSON-String, wie etwa Optionen zum strengen Validieren (z. B. `{"strict": true}`).
- **mode** (string, optional): Der Import-Modus. Standardmäßig `quick`. Unterstützt werden Werte wie `quick`, `full` oder `strict`.

### Request-Beispiel

```json
{
  "source": "{\"host\": \"example.com\", \"import_data\": {\"key\": \"value\"}}",
  "config": "{\"strict\": true}",
  "mode": "quick"
}
```

### Response-Beispiel

```json
{
  "success": true,
  "data": {
    "source": "{\"host\": \"example.com\", \"import_data\": {\"key\": \"value\"}}",
    "config": "{\"strict\": true}",
    "mode": "quick",
    "import_result": {
      "status": "imported",
      "records_processed": 1
    },
    "message": "Hosting data successfully imported."
  },
  "error": null,
  "warnings": [],
  "meta": {}
}
```
