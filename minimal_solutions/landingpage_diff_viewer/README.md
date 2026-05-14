# Landingpage Diff Viewer

Documentation for Landingpage Diff Viewer minimal solution.

## Externe Nutzung / API-Schnittstelle

Diese Minimal-Lösung bietet eine REST-API-Schnittstelle, um Landingpage-Unterschiede programmgesteuert zu analysieren.

**Endpunkt:** `POST /api/minimal-solutions/landingpage_diff_viewer`
**Content-Type:** `application/json`

### Request-Beispiel

```json
{
  "topic": "Produkt-Launch",
  "target": "Neukunden",
  "options": {
    "compare_with": "v1",
    "highlight_changes": true
  }
}
```

### Response-Beispiel

```json
{
  "status": "success",
  "data": {
    "topic": "Produkt-Launch",
    "target": "Neukunden",
    "diff_result": {
      "added": ["Call to Action Button"],
      "removed": ["Alte Preisliste"],
      "modified": ["Header Text"]
    },
    "timestamp": "2026-05-13T12:00:00Z"
  }
}
```
