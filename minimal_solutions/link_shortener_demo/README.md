# Link Shortener Demo

Eine Minimal-Lösung zum Verkürzen von URLs (als Demo). Diese Schnittstelle ermöglicht es, aus langen URLs kurze, handliche Links zu generieren.

## Externe Nutzung (API)

Sie können die Schnittstelle über einen HTTP POST-Request extern ansteuern. Senden Sie dazu ein JSON-Objekt mit der langen URL und optional einem eigenen Wunsch-Slug an den Endpunkt.

**Endpoint:** `POST /api/minimal-solutions/link_shortener_demo`

### Request-Beispiel

```json
{
  "long_url": "https://example.com/very/long/url/path",
  "custom_slug": "mein-link"
}
```

### Response-Beispiel

```json
{
  "status": "success",
  "data": {
    "short_url": "https://short.ly/mein-link",
    "clicks": 0
  }
}
```
