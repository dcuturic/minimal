# SEO Normalizer

Minimal-Lösung für SEO Normalizer.

## Beschreibung
Diese Komponente normalisiert SEO-Daten (wie Titel, Beschreibungen, URLs) basierend auf vorgegebenen Topics und Targets, optional ergänzt durch spezifische Normalisierungsoptionen.

## API Endpoint
`POST /api/minimal-solutions/seo_normalizer`

## Externe Verwendung der Schnittstelle
Dieser Service kann von externen Anwendungen über die HTTP-Schnittstelle als REST-API genutzt werden.

### Request-Beispiel

```json
POST /api/minimal-solutions/seo_normalizer
Content-Type: application/json

{
  "topic": "Technology",
  "target": "Mobile Phones",
  "options": {
    "normalize_strategy": "strict",
    "locale": "de-DE"
  }
}
```

### Response-Beispiel

```json
{
  "status": "success",
  "data": {
    "topic": "Technology",
    "target": "Mobile Phones",
    "options": {
      "normalize_strategy": "strict",
      "locale": "de-DE"
    },
    "normalized_status": "success",
    "normalized_items": 5,
    "message": "Daten für 'Technology' erfolgreich normalisiert."
  }
}
```
