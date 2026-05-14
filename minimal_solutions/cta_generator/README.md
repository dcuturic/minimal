# CTA Generator - Minimal-Lösung

Diese Minimal-Lösung generiert passgenaue Call-to-Action (CTA) Texte basierend auf Thema, Zielgruppe und Tonfall.

## Externe Verwendung (API)

Die Lösung bietet auch eine REST API, die von externen Anwendungen konsumiert werden kann.

### Endpunkt
`POST /api/minimal-solutions/cta_generator`

### Request (JSON)
```json
{
  "topic": "Neuer Sommer-Sale",
  "audience": "Junge Erwachsene",
  "tone": "enthusiastic"
}
```

### Response (JSON)
```json
{
  "status": "success",
  "data": {
    "suggestions": [
      "Shoppe jetzt den Sommer-Sale!",
      "Sichere dir die besten Angebote für junge Erwachsene!"
    ]
  }
}
```
