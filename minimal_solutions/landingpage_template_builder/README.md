# Landingpage Template Builder

Minimal solution for Landingpage Template Builder.

## Externe Nutzung der API / Schnittstelle

Dieser Service bietet einen API-Endpunkt, mit dem Landingpage-Templates programmgesteuert basierend auf einem Thema (Topic) und einer Zielgruppe (Target) generiert werden können. 
Die API kann von externen Applikationen angesprochen werden, um beispielsweise Templates automatisch in einen Website-Builder zu integrieren oder Vorlagen für spezifische Marketing-Kampagnen zu erstellen.

**Endpunkt:**
`POST /api/minimal-solutions/landingpage_template_builder`

### Request-Beispiel
```json
{
  "topic": "Marketing Campaign",
  "target": "B2B Customers",
  "options": {
    "layout": "hero-left",
    "colors": "dark"
  }
}
```

### Response-Beispiel
```json
{
  "status": "success",
  "data": {
    "template_id": "tpl_890123",
    "html": "<div class='hero'>...</div>",
    "css": ".hero { background: #000; }",
    "config": {
      "topic": "Marketing Campaign",
      "target": "B2B Customers"
    }
  }
}
```
