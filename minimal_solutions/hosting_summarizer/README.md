# Hosting Summarizer

Eine Minimal-Lösung zur Zusammenfassung von Hosting-Daten. Diese Schnittstelle kann von externen Systemen über einen POST-Request genutzt werden, um JSON-basiert Hosting-Metrics und Config-Daten zu verarbeiten.

## API Nutzung (Extern)

**Endpoint:** `POST /api/minimal-solutions/hosting_summarizer`
**Content-Type:** `application/json`

Sie können diese API ansteuern, indem Sie die erforderlichen Felder `source`, `config` (optional) und `mode` im JSON-Format senden.

### Request-Beispiel

```json
{
  "source": "{\"host\": \"example.com\", \"metrics\": {\"uptime\": 99.9, \"cpu\": 45}}",
  "config": {},
  "mode": "summary"
}
```

### Response-Beispiel

```json
{
  "success": true,
  "data": {
    "source": "{\"host\": \"example.com\", \"metrics\": {\"uptime\": 99.9, \"cpu\": 45}}",
    "config": {},
    "mode": "summary",
    "summarized": true,
    "status": "success",
    "message": "Hosting erfolgreich zusammengefasst im Modus 'summary'."
  },
  "error": null,
  "warnings": [],
  "meta": {}
}
```
