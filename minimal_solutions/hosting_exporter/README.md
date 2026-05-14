# Hosting Exporter

## Beschreibung
Der **Hosting Exporter** ist eine Minimal-Lösung zum Exportieren von Hosting-Daten. 
Neben der integrierten Benutzeroberfläche stellt das Tool eine API-Schnittstelle bereit, die von externen Systemen aufgerufen werden kann. Externe Systeme können einen `POST`-Request mit den erforderlichen JSON-Parametern senden, um einen Export im gewünschten Modus anzufordern.

## Externe Nutzung (API)

Die Schnittstelle kann problemlos von jedem HTTP-fähigen Client (z. B. cURL, Postman, oder externe Backend-Services) verwendet werden. Senden Sie dazu einfach einen POST-Request mit Content-Type `application/json`.

**Endpoint:** `POST /api/minimal-solutions/hosting_exporter`

### Request-Beispiel

```json
{
  "source": "{\"host\": \"example.com\", \"export_enabled\": true}",
  "config": "{\"strict\": true}",
  "mode": "quick"
}
```

### Response-Beispiel

```json
{
  "success": true,
  "data": {
    "source": "{\"host\": \"example.com\", \"export_enabled\": true}",
    "config": "{\"strict\": true}",
    "mode": "quick",
    "export_result": "...",
    "message": "Hosting successfully exported."
  },
  "error": null,
  "warnings": [],
  "meta": {}
}
```
