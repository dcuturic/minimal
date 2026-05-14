# Hosting Mapper

Minimal-Lösung: Hosting Mapper

## API-Dokumentation

Die Schnittstelle `/api/minimal-solutions/hosting_mapper` ermöglicht das externe Mappen von Hosting-Daten. 

### Endpunkt
`POST /api/minimal-solutions/hosting_mapper`

### Request-Beispiel
```json
{
  "source": "{\"hostings\": [{\"domain\": \"example.com\", \"provider\": \"aws\"}]}",
  "config": {"mapping_rules": {"aws": "Amazon Web Services"}},
  "mode": "default"
}
```

### Response-Beispiel
```json
{
  "success": true,
  "data": {
    "source": "{\"hostings\": [{\"domain\": \"example.com\", \"provider\": \"aws\"}]}",
    "config": {
      "mapping_rules": {
        "aws": "Amazon Web Services"
      }
    },
    "mode": "default",
    "mapped": true,
    "status": "success",
    "message": "Hosting erfolgreich gemappt im Modus 'default'."
  },
  "error": null,
  "warnings": [],
  "meta": {}
}
```

### Externe Verwendung
Senden Sie einen HTTP POST-Request mit einem JSON-Body an die API. Die Felder `source`, `config` (optional) und `mode` steuern den Mapping-Prozess. Die API gibt ein standardisiertes JSON-Objekt zurück, das im Erfolgsfall die transformierten (gemappten) Daten unter dem `data`-Key enthält.
