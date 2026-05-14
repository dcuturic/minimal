# Hosting Checker

Der "Hosting Checker" ist eine Minimal-Lösung zur einfachen Überprüfung von Hosting-Daten.

## Externe Nutzung (API)

Die Schnittstelle kann von externen Systemen aufgerufen werden, indem ein HTTP-POST-Request an den API-Endpunkt gesendet wird. Die Parameter müssen als JSON-Body übergeben werden.

**Endpoint:**
`POST /api/minimal-solutions/hosting_checker`

### Parameter

- `source` (string, required): Die zu überprüfenden Hosting-Daten, meistens als JSON-String.
- `config` (string, optional): Zusätzliche Konfigurationen (z.B. für detaillierte Prüfungen).
- `mode` (string, required): Der Prüfmodus, z.B. `quick`, `full` oder `strict`.

### Request-Beispiel

```json
{
  "source": "{\"host\": \"example.com\", \"type\": \"shared\"}",
  "config": "{\"strict\": true}",
  "mode": "quick"
}
```

### Response-Beispiel

```json
{
  "success": true,
  "data": {
    "source": "{\"host\": \"example.com\", \"type\": \"shared\"}",
    "config": "{\"strict\": true}",
    "mode": "quick",
    "check_result": "...",
    "message": "Hosting successfully checked."
  },
  "error": null,
  "warnings": [],
  "meta": {}
}
```
