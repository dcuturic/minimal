# SEO Checker

Eine Minimal-Lösung zur Überprüfung von SEO-Metriken einer gegebenen URL für ein bestimmtes Keyword.

## Externe API-Nutzung

Die SEO Checker API kann von externen Diensten konsumiert werden, um automatisiert SEO-Daten zu prüfen. 

### Endpunkt
`POST /api/minimal-solutions/seo_checker`

### Request-Beispiel
Sende einen `POST`-Request mit einem JSON-Body, der die Parameter `topic`, `target` und `options` enthält.

```json
{
  "topic": "https://example.com",
  "target": "Desktop",
  "options": ["check_density"]
}
```

### Response-Beispiel
Die API antwortet in einem standardisierten JSON-Format mit einem `status` und den `data` der SEO-Prüfung.

```json
{
  "status": "success",
  "data": {
    "score": 85,
    "issues": [],
    "keyword_density": "2.5%"
  }
}
```

## Struktur

- `seo_checker_ui.py`: UI für die Lösung.
- `seo_checker_api.py`: API Backend Logik.
- `seo_checker_validation.py`: Validierung der API Requests.
- `demo.json`: Beispiel Daten.
