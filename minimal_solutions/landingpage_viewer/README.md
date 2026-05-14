# Landingpage Viewer

Der Landingpage Viewer ist eine Minimal-Lösung zur einfachen Anzeige und Kontrolle von Landingpage-Informationen. Diese Lösung ist in die CraftHoster Plattform integriert und steht auch als REST-API zur Verfügung.

## Externe API-Nutzung

Die Schnittstelle kann problemlos von externen Systemen und Skripten konsumiert werden, um Landingpage-Daten automatisiert zu verarbeiten oder anzuzeigen. Sende dazu einfach einen POST-Request mit den entsprechenden Datenpaketen an den API-Endpunkt.

### Endpoint
`POST /api/minimal-solutions/landingpage_viewer`

### Request-Beispiel
```json
{
  "topic": "Modern AI SaaS",
  "target": "Developers and Tech Founders",
  "options": "Check spelling, check CTA"
}
```

### Response-Beispiel
```json
{
  "status": "success",
  "data": {
    "view_result": "Landingpage Data View:\n\nTopic: Modern AI SaaS\nTarget Audience: Developers and Tech Founders\nOptions: Check spelling, check CTA",
    "meta": {
      "topic": "Modern AI SaaS",
      "target": "Developers and Tech Founders",
      "options": "Check spelling, check CTA"
    }
  }
}
```
