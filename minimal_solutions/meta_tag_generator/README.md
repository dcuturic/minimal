# Meta Tag Generator

Eine Minimal-Lösung zur Generierung von HTML Meta Tags.

## Externe Nutzung

Die Meta Tag Generator API kann in externen Applikationen verwendet werden, um dynamisch Meta Tags für Webseiten zu generieren. Durch Senden eines `POST`-Requests mit Titel, Beschreibung und optionalen Bild-/Seiten-URLs werden die fertigen HTML-Meta-Tags im JSON-Format zurückgegeben. Dies ist besonders nützlich für CMS-Systeme oder automatisierte Skripte, die SEO-relevante Metadaten benötigen.

### API Endpunkt

`POST /api/minimal-solutions/meta_tag_generator`

### Request Beispiel

```json
{
  "title": "CraftHoster - Minimal Solutions",
  "description": "Die besten Minimal-Lösungen für Entwickler.",
  "image_url": "https://crafthoster.com/preview.jpg",
  "page_url": "https://crafthoster.com/solutions"
}
```

### Response Beispiel

```json
{
  "status": "success",
  "data": {
    "html": "<title>CraftHoster - Minimal Solutions</title>\n<meta name=\"description\" content=\"Die besten Minimal-Lösungen für Entwickler.\">\n<!-- weitere Tags... -->"
  }
}
```
