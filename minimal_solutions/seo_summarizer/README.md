# SEO Summarizer

Der SEO Summarizer ist eine Minimal-Lösung, um SEO-relevante Daten (URLs, Texte) zu analysieren und in gewünschte Zielformate (z.B. Management Summaries, Bullet Points) zusammenzufassen.

## Externe API-Nutzung

Die Schnittstelle kann problemlos von externen Systemen (z.B. per `curl`, `fetch` oder Python `requests`) verwendet werden, um automatisierte Zusammenfassungen zu generieren. Senden Sie dazu einfach einen POST-Request an den entsprechenden Endpunkt mit den erforderlichen JSON-Daten.

### Endpunkt
`POST /api/minimal-solutions/seo_summarizer`

### Request-Beispiel

```json
{
  "topic": "https://example.com/blog-post",
  "target": "Management Summary",
  "options": [
    "extract_keywords",
    "include_metrics"
  ]
}
```

### Response-Beispiel

```json
{
  "status": "success",
  "data": {
    "summary": "Die Seite behandelt grundlegende SEO-Metriken und Best Practices...",
    "key_findings": [
      "Wichtigkeit von Meta-Tags",
      "Optimierung der Ladezeiten"
    ],
    "extracted_keywords": [
      "SEO",
      "Best Practices",
      "Performance"
    ]
  }
}
```
