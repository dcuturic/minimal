# Headline Generator

Ein Tool zum automatischen Generieren von ansprechenden und klickstarken Headlines (Überschriften) basierend auf einem Thema und gewünschtem Stil. Ideal für Artikel, Ads oder Posts.

## Verwendung als API

Die Headline Generator-Schnittstelle kann problemlos in externe Systeme integriert werden. Sende dazu einen POST-Request an den entsprechenden Endpunkt mit einem JSON-Body, der das gewünschte Thema (`topic`), den Stil (`style`) und die Anzahl (`count`) enthält.

**Endpoint:** `POST /api/minimal-solutions/headline_generator`

### Request-Beispiel

```json
{
  "topic": "Artificial Intelligence",
  "style": "clickbait",
  "count": 3
}
```

### Response-Beispiel

```json
{
  "status": "success",
  "data": {
    "headlines": [
      "10 Mind-Blowing Facts About Artificial Intelligence",
      "Why Artificial Intelligence is the Future",
      "Artificial Intelligence: What You Need to Know"
    ]
  }
}
```

### Mögliche Stile
- `informative` (Informativ)
- `clickbait` (Clickbait)
- `humorous` (Humorvoll)
- `provocative` (Provokativ)
- `professional` (Professionell)

### Limits
- `count` kann maximal 10 betragen und muss mindestens 1 sein.
- `topic` muss ein gültiger Text sein.
