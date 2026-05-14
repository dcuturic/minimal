# SEO Template Builder

Dieses Modul stellt eine Minimal-Lösung ("SEO Template Builder") dar, um aus einem Basis-Thema (Topic), einer Zielgruppe (Target) und optionalen Parametern ein initiales Template für SEO-Zwecke zu generieren.

## Externe API-Nutzung

Die Kernfunktionalität dieses Tools steht als REST-API zur Verfügung. Externe Applikationen oder Services können via HTTP POST-Requests mit dem Builder kommunizieren und programmatisch Templates anfordern.

### Endpunkt

**POST** `/api/minimal-solutions/seo_template_builder`

### Request-Beispiel

Die Anfrage erwartet einen JSON-Body mit dem Thema (`topic`), der Zielgruppe (`target`) und optionalen Einstellungen (`options`):

```json
{
  "topic": "E-commerce SEO Strategy",
  "target": "Online Store Owners",
  "options": {
    "format": "json",
    "language": "en"
  }
}
```

### Response-Beispiel

Die API gibt die verarbeiteten Datenstrukturen standardisiert im `data`-Feld zurück:

```json
{
  "status": "success",
  "data": {
    "topic": "E-commerce SEO Strategy",
    "target": "Online Store Owners",
    "template_status": "success",
    "message": "Template für 'E-commerce SEO Strategy' erfolgreich generiert.",
    "options_applied": {
      "format": "json",
      "language": "en"
    }
  }
}
```
