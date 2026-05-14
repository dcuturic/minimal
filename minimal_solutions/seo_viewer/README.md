# SEO Viewer

Diese Minimal-Lösung bietet eine einfache Möglichkeit, SEO-relevante Daten zu visualisieren. 

## API-Dokumentation

Die Schnittstelle kann extern verwendet werden, um SEO-Daten automatisiert zu übermitteln und verarbeitet zurückzuerhalten.

**Endpunkt:**
`POST /api/minimal-solutions/seo_viewer`

**Header:**
- `Content-Type: application/json`

### Request-Beispiel

```json
{
  "topic": "https://example.com",
  "target": "Desktop",
  "options": [
    "extract_meta"
  ]
}
```

### Response-Beispiel

```json
{
  "status": "success",
  "data": {
    "title": "Example Domain",
    "description": "An example domain for illustrations.",
    "keywords": ["example", "domain"]
  }
}
```

### Externe Verwendung
Um die Schnittstelle in Ihre eigene Applikation einzubinden, senden Sie einfach einen POST-Request mit einem gültigen JSON-Body an den oben genannten Endpunkt. Das System validiert die Eingaben (`topic`, `target` und `options`) und liefert die aufbereiteten Daten im `data`-Objekt der Response zurück. Im Fehlerfall wird ein entsprechendes Error-JSON mit einer aussagekräftigen Fehlermeldung generiert.
