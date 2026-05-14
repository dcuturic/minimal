# Markdown Preview

Ein Minimal-Lösung Tool zum Anzeigen von Markdown als HTML.
Bietet eine Live-Vorschau und die Möglichkeit, das generierte HTML zu kopieren.

## Externe API Nutzung

Die Markdown Preview Lösung kann auch von externen Applikationen über eine REST-API genutzt werden. Senden Sie einfach einen POST-Request mit dem Markdown-Text an den Endpoint.

**Endpoint:** `POST /api/minimal-solutions/markdown_preview`

### Request (JSON)
```json
{
  "markdown_text": "# Hello\n\n**World**"
}
```

### Response (JSON)
```json
{
  "status": "success",
  "data": {
    "html": "<h1>Hello</h1>\n<p><strong>World</strong></p>"
  }
}
```

## Fehlerbehandlung
Wenn das Feld `markdown_text` fehlt, gibt die API einen 400 Bad Request Fehler zurück:
```json
{
  "status": "error",
  "message": "Feld 'markdown_text' ist erforderlich."
}
```
