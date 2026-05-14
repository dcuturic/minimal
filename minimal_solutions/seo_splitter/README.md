# SEO Splitter

Dieses Tool teilt SEO-relevante Inhalte (Topics und Targets) basierend auf benutzerdefinierten Optionen auf. Es ist als minimale API-Lösung konzipiert und kann extern über eine HTTP POST-Anfrage angesprochen werden.

## Externe API-Nutzung

Die Schnittstelle lässt sich von externen Systemen (wie anderen Web-Apps, Automatisierungsscripten oder CLI-Tools) ansprechen.

**Endpunkt:**
`POST /api/minimal-solutions/seo_splitter`

**Content-Type:** `application/json`

### Request-Beispiel

```json
{
  "topic": "Content Marketing",
  "target": "Beginners",
  "options": {
    "split_by": "paragraphs"
  }
}
```

### Response-Beispiel

```json
{
  "status": "success",
  "data": {
    "result": "..."
  }
}
```
