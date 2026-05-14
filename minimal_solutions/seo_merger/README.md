# SEO Merger

Minimal solution for SEO Merger.

## Externe Nutzung / API Dokumentation

Die SEO Merger Schnittstelle kann extern als API genutzt werden, um SEO-Daten basierend auf Topic, Target und weiteren Optionen zusammenzuführen (Merger). 

### API Endpoint
`POST /api/minimal-solutions/seo_merger`

### Request-Beispiel

```json
{
  "topic": "Technology",
  "target": "Mobile Phones",
  "options": {
    "merge_strategy": "combine",
    "locale": "de-DE"
  }
}
```

Die Felder `topic` und `target` sind optional, genau wie `options`.

### Response-Beispiel

```json
{
  "status": "success",
  "data": {
    "topic": "Technology",
    "target": "Mobile Phones",
    "options": {
      "merge_strategy": "combine",
      "locale": "de-DE"
    },
    "status": "success",
    "message": "Daten für 'Technology' erfolgreich verarbeitet."
  }
}
```
