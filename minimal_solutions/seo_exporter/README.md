# SEO Exporter

Der **SEO Exporter** ist eine Minimal-Lösung, mit der sich SEO-bezogene Daten in verschiedene Formate (z. B. CSV, JSON, XML) exportieren lassen. 

## Externe API-Nutzung

Die Schnittstelle kann problemlos von externen Diensten angesprochen werden, indem ein `POST`-Request an den Endpunkt gesendet wird.

### Endpunkt

`POST /api/minimal-solutions/seo_exporter`

### Request-Beispiel

Sende einen JSON-Payload mit den Feldern `topic` (Eingabedaten), `target` (Zielformat) und optionalen `options` (z.B. Formatierungsoptionen).

```json
{
  "topic": "https://example.com/blog",
  "target": "CSV",
  "options": [
    "include_meta",
    "format_date"
  ]
}
```

### Response-Beispiel

Die API antwortet standardmäßig mit einem JSON-Objekt, das den Status sowie die exportierten Daten im gewünschten Format enthält.

```json
{
  "status": "success",
  "data": {
    "exported_format": "CSV",
    "content": "url,title,description\nhttps://example.com/blog,Blog,Der Blog"
  }
}
```
