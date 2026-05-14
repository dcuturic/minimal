# SEO Formatter

Die "SEO Formatter" Minimal-Lösung ermöglicht es, Rohtext oder Themen-Keywords in ein optimales Format für verschiedene Suchmaschinen oder Social Media Plattformen umzuwandeln. Es hilft dabei, den Text hinsichtlich Lesbarkeit und Keyword-Hervorhebung (z.B. durch `<b>`-Tags) aufzubereiten.

## API-Schnittstelle

Die Funktionalität kann nicht nur über die UI genutzt werden, sondern steht auch als REST-API zur Verfügung. Dies ermöglicht die einfache Integration des SEO Formatters in externe Tools, Skripte oder andere Applikationen.

### Endpunkt

`POST /api/minimal-solutions/seo_formatter`

### Request-Beispiel

Die API erwartet einen JSON-Payload mit den folgenden Feldern:
- `topic` (String, erforderlich): Der Rohtext oder das Thema.
- `target` (String, erforderlich): Das Ziel, für das optimiert werden soll (z.B. Google, Bing, Facebook).
- `options` (Array of Strings, optional): Zusätzliche Verarbeitungsoptionen (z.B. `["bold_keywords", "clean_html"]`).

```json
{
  "topic": "Wie man den besten Pizzateig selber macht: Ein Rezept",
  "target": "Google",
  "options": ["bold_keywords", "clean_html"]
}
```

### Response-Beispiel

Die API gibt im Erfolgsfall eine standardisierte JSON-Antwort zurück, welche die formatierten Daten im `data`-Objekt enthält.

```json
{
  "status": "success",
  "data": {
    "formatted_content": "<h2>Wie man den <b>besten Pizzateig</b> selber macht: Ein Rezept</h2>\n<p>Ein guter Pizzateig braucht Zeit und Liebe...</p>",
    "metadata": {
      "target": "Google",
      "applied_options": ["bold_keywords", "clean_html"]
    }
  }
}
```

### Fehlerbehandlung

Bei Fehlern (z.B. fehlende Pflichtfelder) liefert die API einen entsprechenden Fehlerstatus mit einer Beschreibung:

```json
{
  "status": "error",
  "message": "Feld 'topic' ist erforderlich."
}
```
