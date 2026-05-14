# SEO Masker

Minimal solution for SEO Masker. This service provides an interface to mask sensitive SEO data based on a given topic, target, and configuration options. It is designed to be easily accessible as an external API.

## API / Schnittstelle

Dieser Service kann extern als API genutzt werden, um SEO-Daten basierend auf Topic, Target und weiteren Optionen zu maskieren.

**Endpunkt:**
`POST /api/minimal-solutions/seo_masker`

### Request-Beispiel
```json
{
  "topic": "Technology",
  "target": "Mobile Phones",
  "options": {
    "mask_level": "high",
    "locale": "de-DE"
  }
}
```

### Response-Beispiel
```json
{
  "status": "success",
  "data": {
    "masked_topic": "T********y",
    "masked_target": "M***********s",
    "mask_level_applied": "high",
    "timestamp": "2024-05-14T12:00:00Z"
  }
}
```
