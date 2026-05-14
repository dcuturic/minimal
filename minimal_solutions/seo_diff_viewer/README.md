# SEO Diff Viewer

Der **SEO Diff Viewer** ist ein Minimal-Service zum Vergleichen zweier SEO-Datensätze (z.B. Original und Ziel/Optimiert). Die Schnittstelle kann extern genutzt werden, um schnell Abweichungen, Fehler oder Optimierungserfolge zwischen zwei Zuständen sichtbar zu machen.

## Externe Nutzung (API)

Dieser Service bietet einen POST-Endpunkt, an den Sie die zu vergleichenden SEO-Daten senden können. Er antwortet mit strukturierten JSON-Daten, die Auskunft über den Status und (in einer vollständigen Implementierung) die detaillierten Unterschiede geben.

**Endpunkt:**
`POST /api/minimal-solutions/seo_diff_viewer`

**Content-Type:** `application/json`

### Request-Beispiel

```json
{
  "topic": "Original SEO Title | Best Store",
  "target": "Updated SEO Title - Best Store",
  "options": {
    "ignore_case": true,
    "ignore_whitespace": true
  }
}
```

### Response-Beispiel

```json
{
  "status": "success",
  "data": {
    "topic": "Original SEO Title | Best Store",
    "target": "Updated SEO Title - Best Store",
    "diff_status": "success",
    "message": "Diff für 'Original SEO Title | Best Store' erfolgreich berechnet.",
    "options_applied": {
      "ignore_case": true,
      "ignore_whitespace": true
    }
  }
}
```
