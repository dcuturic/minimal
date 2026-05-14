# Hosting Masker

Eine Minimal-Lösung, um sensible Hosting-Daten (wie IP-Adressen, Hostnamen, Benutzer) sicher zu maskieren, um sie beispielsweise für Demos oder Logs unkenntlich zu machen.

## Externe Nutzung (API)

Die Schnittstelle kann von externen Systemen (z. B. anderen Microservices, CI/CD-Pipelines oder Frontend-Applikationen) aufgerufen werden, indem ein `POST`-Request mit den entsprechenden Parametern als JSON-Body gesendet wird. 

**Endpoint:** `POST /api/minimal-solutions/hosting_masker`
**Content-Type:** `application/json`

### Parameter
- `source` (String): Die zu maskierenden Hosting-Daten (z. B. als JSON-String). Pflichtfeld.
- `config` (String): Optionale Konfigurationseinstellungen für den Maskierungsvorgang (z. B. Maskierungszeichen).
- `mode` (String): Der Maskierungsmodus (z. B. `partial`, `full`). Standard ist `partial`.

### Request-Beispiel

```json
{
  "source": "{\"host\": \"example.com\", \"ip\": \"192.168.1.1\", \"user\": \"admin\"}",
  "config": "{\"maskChar\": \"*\"}",
  "mode": "partial"
}
```

### Response-Beispiel

```json
{
  "success": true,
  "data": {
    "source": "{\"host\": \"example.com\", \"ip\": \"192.168.1.1\", \"user\": \"admin\"}",
    "config": "{\"maskChar\": \"*\"}",
    "mode": "partial",
    "masked_data": "{\"host\": \"ex*****.com\", \"ip\": \"192.168.*.*\", \"user\": \"ad***\"}",
    "message": "Hosting data successfully masked."
  },
  "error": null,
  "warnings": [],
  "meta": {}
}
```

## Lokale Nutzung

1. Starte den Web-Server.
2. Öffne die UI unter `/minimal-solutions/hosting_masker` im Browser.
3. Füge die zu maskierenden Daten im `Source`-Feld ein.
4. Wähle den gewünschten Modus und klicke auf "Maskieren".
