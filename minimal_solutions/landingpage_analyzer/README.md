# Landingpage Analyzer

Eine Minimal-Lösung zur Analyse von Landingpages bezüglich Zielgruppen, Themen sowie SEO, Performance und UX-Mustern.

## Externe Nutzung der Schnittstelle (API)

Die Lösung bietet einen REST-API-Endpunkt, der von externen Applikationen verwendet werden kann, um Daten automatisiert analysieren zu lassen.

**Endpunkt:**
`POST /api/minimal-solutions/landingpage_analyzer`

**Header:**
- `Content-Type: application/json`

### Request-Beispiel

```json
{
  "topic": "Modern AI SaaS",
  "target": "Developers and Tech Founders",
  "options": "Analyze SEO, performance, UX patterns"
}
```

### Response-Beispiel

```json
{
  "status": "success",
  "data": {
    "analyzed_data": {
      "seo_score": 85,
      "performance": "Good",
      "suggestions": [
        "Include relevant keywords in the H1 tag.",
        "Optimize images for faster load times.",
        "Implement clear call-to-actions for the target audience."
      ]
    },
    "meta": {
      "topic": "Modern AI SaaS",
      "target": "Developers and Tech Founders"
    }
  }
}
```
