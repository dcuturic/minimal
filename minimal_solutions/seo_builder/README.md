# SEO Builder

Eine Minimal-Lösung, die SEO-Daten für ein bestimmtes Thema und eine Zielplattform (z.B. Google, Blog) generiert. Diese Lösung ist sowohl über eine interaktive Benutzeroberfläche als auch als direkte API-Schnittstelle nutzbar.

## Externe Nutzung (API)

Die Lösung kann von externen Applikationen, Skripten oder Diensten über den Endpunkt `/api/minimal-solutions/seo_builder` angesprochen werden. Hierfür muss ein HTTP `POST` Request mit dem `Content-Type: application/json` gesendet werden.

### Parameter

- **topic** (String, erforderlich): Das Thema oder der Rohtext, für den SEO-Daten generiert werden sollen.
- **target** (String, erforderlich): Die Zielplattform oder das Medium (z.B. "Google", "Blog", "Landing Page").
- **options** (Array/List of Strings, optional): Zusätzliche Optionen für die SEO-Generierung (z.B. `["keywords", "meta_tags"]`).

### Request Beispiel

```http
POST /api/minimal-solutions/seo_builder
Content-Type: application/json

{
  "topic": "Dein Thema hier...",
  "target": "Google",
  "options": ["keywords", "meta_tags"]
}
```

### Response Beispiel

Die API antwortet im Standard-JSON-Format der Plattform:

```json
{
  "status": "success",
  "data": {
    "title": "Optimierter Titel",
    "description": "Optimierte Beschreibung",
    "keywords": ["seo", "builder", "demo"]
  }
}
```

## UI-Komponente

Die Benutzeroberfläche ermöglicht es, die API interaktiv zu testen. Sie bietet:
- Ein Formular für die Eingabe von Thema, Ziel und Optionen.
- Eine Live-Ladeanzeige während der Verarbeitung.
- Eine formatierte Ergebnisansicht mit Copy- und Download-Funktionen.
- Eine integrierte API-Dokumentation direkt in der UI.
