# Landingpage Builder

Minimal Solution für den Landingpage Builder. Mit dieser Lösung kannst du automatisiert einfache Landingpage-Grundgerüste (HTML) anhand von Thema und Zielgruppe erstellen.

## Externe API-Nutzung

Diese Schnittstelle kann von externen Systemen, CMS oder Automatisierungstools angesprochen werden, um schnell HTML-Code für Landingpages zu generieren. Sende einen POST-Request mit dem gewünschten Thema (topic), der Zielgruppe (target) und optionalen Einstellungen (options) im JSON-Format. Als Antwort erhältst du generiertes HTML-Markup, das du direkt in deine Applikation einbetten kannst.

### Endpoint

`POST /api/minimal-solutions/landingpage_builder`

### Request-Beispiel

```json
{
  "topic": "Modern Web Development",
  "target": "Frontend Developers",
  "options": {
    "theme": "dark",
    "features": ["SEO", "Responsive"]
  }
}
```

### Response-Beispiel

```json
{
  "status": "success",
  "data": {
    "html": "<div class=\"landing-page\">\n  <header class=\"hero dark\">\n    <h1>Modern Web Development</h1>\n    <p>Tailored for Frontend Developers</p>\n  </header>\n  <section class=\"features\">\n    <div class=\"feature\">SEO</div>\n    <div class=\"feature\">Responsive</div>\n  </section>\n</div>"
  }
}
```
