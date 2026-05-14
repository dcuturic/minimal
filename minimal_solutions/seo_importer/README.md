# SEO Importer

Minimal-Lösung für SEO Importer.

## Externe API-Nutzung

Die Schnittstelle kann als REST-API verwendet werden, um SEO-Daten basierend auf einem bestimmten Thema und Ziel zu importieren.

### Endpunkt

`POST /api/minimal-solutions/seo_importer`

### Request-Beispiel

```json
{
  "topic": "Content Marketing",
  "target": "B2B",
  "options": {
    "strict": true
  }
}
```

### Response-Beispiel

```json
{
  "status": "success",
  "data": {
    "topic": "Content Marketing",
    "target": "B2B",
    "options": {
      "strict": true
    },
    "import_status": "success",
    "imported_items": 42,
    "message": "Daten für 'Content Marketing' erfolgreich importiert."
  }
}
```
