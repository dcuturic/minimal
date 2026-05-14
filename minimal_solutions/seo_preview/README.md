# SEO Preview - Minimal Lösung

Diese Minimal-Lösung bietet eine Vorschau für SEO-Daten basierend auf einem Thema und Ziel-Plattform. 
Sie kann über die Benutzeroberfläche verwendet werden oder als externe API-Schnittstelle in andere Anwendungen integriert werden.

## API-Schnittstelle extern verwenden

Du kannst die Schnittstelle extern verwenden, indem du einen POST-Request an den Endpoint sendest. Dadurch lässt sich die SEO-Vorschau in Drittanwendungen oder externe Skripte integrieren.

**Endpoint:** `POST /api/minimal-solutions/seo_preview`
**Content-Type:** `application/json`

### Request Beispiel

```json
{
  "topic": "Dein Text oder Thema...",
  "target": "Google",
  "options": ["desktop", "mobile"]
}
```

### Response Beispiel

```json
{
  "status": "success",
  "data": {
    "preview": "Vorschau-Daten generiert anhand der übergebenen Parameter.",
    "metadata": {
      "target": "Google",
      "options_used": ["desktop", "mobile"]
    }
  }
}
```
