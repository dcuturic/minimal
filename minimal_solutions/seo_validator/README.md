# SEO Validator

Der **SEO Validator** ist eine Minimal-Lösung zur Validierung von SEO-Daten (Titel, Meta-Descriptions, Keywords etc.) basierend auf definierten Regeln für verschiedene Plattformen. Die Lösung kann sowohl über die UI als auch extern über die API-Schnittstelle genutzt werden.

## API-Schnittstelle

Die API kann von externen Anwendungen oder Skripten aufgerufen werden, um SEO-Metadaten automatisiert zu überprüfen. 

### Endpunkt
`POST /api/minimal-solutions/seo_validator`

### Request-Beispiel
Sende einen POST-Request mit den zu validierenden Daten im JSON-Format:

```json
{
  "topic": "Ein sehr langer und detaillierter Text, der als Meta-Description dienen soll, aber eventuell die maximale Länge für Google-Ergebnisse überschreitet...",
  "target": "Google",
  "options": ["strict", "verbose"]
}
```

**Parameter:**
- **`topic`** (String, required): Der zu validierende Text, Titel oder Metadaten-Inhalt.
- **`target`** (String, required): Zielplattform oder System (z.B. Google, Bing, Social Media), nach deren Regeln validiert werden soll.
- **`options`** (Array of Strings, optional): Zusätzliche Parameter für die Validierung (z.B. "strict", "verbose").

### Response-Beispiel
Die API antwortet in einem einheitlichen JSON-Format:

```json
{
  "status": "success",
  "data": {
    "is_valid": true,
    "issues": [],
    "score": 95,
    "metadata": {
      "target": "Google"
    }
  }
}
```
