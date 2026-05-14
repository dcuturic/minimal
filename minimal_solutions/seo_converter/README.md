# SEO Converter

Die **SEO Converter** Minimal-Lösung ermöglicht es, rohe SEO-Daten (wie JSON oder Text) in andere Zielformate (z.B. XML, CSV) zu konvertieren.

## Externe Verwendung der API

Die Schnittstelle kann problemlos von externen Diensten und Microservices angesprochen werden. Durch das Senden eines POST-Requests mit den erforderlichen Parametern können automatisierte Pipelines die Konvertierung von SEO-Daten durchführen.

### API Endpoint

`POST /api/minimal-solutions/seo_converter`

### Request-Beispiel

```json
{
  "topic": "{\"title\": \"My Title\", \"description\": \"My SEO Description\"}",
  "target": "XML",
  "options": ["pretty_print"]
}
```

### Response-Beispiel (Erfolgreich)

```json
{
  "status": "success",
  "data": {
    "result": "<seo>\n  <title>My Title</title>\n  <description>My SEO Description</description>\n</seo>"
  }
}
```

### Response-Beispiel (Fehler)

```json
{
  "status": "error",
  "message": "Feld 'target' darf nicht leer sein."
}
```
