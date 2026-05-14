# Landingpage Exporter

Eine Minimal-Lösung, um Landingpages in verschiedenen Formaten zu exportieren. Die API-Schnittstelle kann von externen Systemen (z.B. CMS, Automatisierungs-Tools oder Build-Pipelines) aufgerufen werden, um auf Basis von Themen und Zielgruppen Landingpage-Inhalte automatisiert zu generieren und im gewünschten Format (z.B. JSON) zurückzuerhalten.

## API-Endpunkt

**POST** `/api/minimal-solutions/landingpage_exporter`

### Request-Beispiel (JSON)

```json
{
  "topic": "Modern AI SaaS",
  "target": "Developers and Tech Founders",
  "options": "JSON format, include SEO headers"
}
```

### Response-Beispiel (JSON)

```json
{
  "status": "success",
  "data": {
    "export_result": "{\n  \"topic\": \"Modern AI SaaS\",\n  \"target\": \"Developers and Tech Founders\",\n  \"options\": \"JSON format, include SEO headers\",\n  \"exported_at\": \"2026-05-13T12:00:00Z\"\n}",
    "meta": {
      "topic": "Modern AI SaaS",
      "target": "Developers and Tech Founders",
      "options": "JSON format, include SEO headers"
    }
  }
}
```
