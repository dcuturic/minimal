# HTML Escape Unescape

Ein einfaches Tool, um HTML-Sonderzeichen in Entities umzuwandeln (Escape) oder HTML-Entities wieder in normale Zeichen zurückzuwandeln (Unescape). Es schützt Webanwendungen vor Cross-Site Scripting (XSS), indem es potenziell gefährliche Zeichen unschädlich macht.

## API Schnittstelle

Diese Minimal-Lösung kann auch problemlos extern über die REST-API angesprochen werden.

### Endpunkt
`POST /api/minimal-solutions/html_escape_unescape`

### Wie die Schnittstelle extern verwendet werden kann
Sende einen `POST`-Request mit einem JSON-Body an den oben genannten Endpunkt. Das JSON muss die Felder `html_text` (den zu verarbeitenden Text) und `mode` (`escape` oder `unescape`) enthalten. Die API antwortet mit einem standardisierten JSON-Objekt, welches das Ergebnis im `data.result`-Feld enthält.

### Request Beispiel

```json
{
  "html_text": "<div class=\"test\">Hello World!</div>",
  "mode": "escape"
}
```

### Response Beispiel

```json
{
  "status": "success",
  "data": {
    "result": "&lt;div class=&quot;test&quot;&gt;Hello World!&lt;/div&gt;"
  }
}
```
