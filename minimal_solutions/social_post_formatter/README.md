# Social Post Formatter

Minimal solution for Social Post Formatter.
Diese API formatiert Texte für verschiedene Social Media Plattformen und fügt spezifische Hashtags hinzu.

## API Integration

Diese Minimal-Lösung kann auch direkt als API in externe Anwendungen integriert werden.

**Endpoint:** `POST /api/minimal-solutions/social_post_formatter`

### Request (JSON)

```json
{
  "platform": "linkedin",
  "text": "My awesome new blog post is live!"
}
```

### Response (JSON)

```json
{
  "status": "success",
  "data": {
    "result": {
      "platform": "linkedin",
      "formatted_text": "My awesome new blog post is live!\n\n---\n#Business #Leadership #Professional",
      "original_text": "My awesome new blog post is live!"
    }
  }
}
```
