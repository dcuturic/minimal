# SEO Generator

Minimal-Lösung: SEO Generator.

## API Usage

Diese Minimal-Lösung bietet eine API-Schnittstelle, die extern genutzt werden kann, um automatisch SEO-Daten basierend auf einem Thema und einer Zielgruppe zu generieren.

**Endpoint:** `POST /api/minimal-solutions/seo_generator`
**Content-Type:** `application/json`

### Request-Beispiel

```json
{
  "topic": "Gaming Chairs",
  "target": "Hardcore Gamers",
  "options": {
    "language": "de",
    "tone": "excited"
  }
}
```

### Response-Beispiel

```json
{
  "status": "success",
  "data": {
    "meta_title": "Top Gaming Chairs for Hardcore Gamers 2026",
    "meta_description": "Upgrade your setup! Discover the best gaming chairs for hardcore gamers...",
    "keywords": [
      "Gaming Chairs",
      "Hardcore Gamers",
      "Ergonomic Gaming",
      "PC Setup"
    ]
  }
}
```
