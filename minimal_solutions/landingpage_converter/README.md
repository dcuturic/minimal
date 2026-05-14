# Landingpage Converter

Eine Minimal-Lösung zur einfachen und schnellen Konvertierung von Landingpage-Daten.
Diese Lösung nimmt die Kernpunkte eines Produkts/Service auf und gibt strukturierte Inhalte (Headline, Subheadline, Features) zurück.

## Externe Schnittstellen-Nutzung (API)

Die Lösung bietet eine standardisierte REST-API, die von externen Applikationen genutzt werden kann.

### Endpunkt

`POST /api/minimal-solutions/landingpage_converter`

### Request-Format (JSON)

Senden Sie einen POST-Request mit folgendem Body:

```json
{
  "topic": "Modern AI SaaS",
  "target": "Developers and Tech Founders",
  "options": "Dark mode, easy integration, low latency"
}
```

### Response-Format (JSON)

Die API antwortet asynchron bzw. konvertiert die Parameter und liefert das Ergebnis im Standard-JSON-Format der Plattform zurück:

```json
{
  "status": "success",
  "data": {
    "converted_data": {
      "headline": "...",
      "subheadline": "...",
      "features": ["..."]
    },
    "meta": {
      "topic": "Modern AI SaaS",
      "target": "Developers and Tech Founders"
    }
  }
}
```

Im Fehlerfall (z. B. bei fehlenden Parametern) liefert die API ein entsprechendes Error-JSON mit `status: "error"` und den zugehörigen `details`.
