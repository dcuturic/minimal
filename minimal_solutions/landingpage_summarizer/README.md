# Landingpage Summarizer

## Beschreibung
Diese Minimal-Lösung ermöglicht es, eine Landingpage basierend auf einem Thema, einer Zielgruppe und optionalen Anweisungen zusammenzufassen.

## Externe Schnittstelle (API)
Die Funktionalität kann über eine REST-API extern genutzt werden. Sende dazu einen POST-Request mit den entsprechenden Daten im JSON-Format an den Endpunkt.

**Endpunkt:**
`POST /api/minimal-solutions/landingpage_summarizer`

### Request-Beispiel
```json
{
  "topic": "Modern AI SaaS",
  "target": "Developers and Tech Founders",
  "options": "Highlight pricing"
}
```

### Response-Beispiel
```json
{
  "status": "success",
  "data": {
    "summary": "This modern AI SaaS targets developers...",
    "key_points": [
      "Point 1",
      "Point 2"
    ],
    "meta": {
      "topic": "Modern AI SaaS",
      "target": "Developers and Tech Founders"
    }
  }
}
```
