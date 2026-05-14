# Hosting Validator

## Beschreibung
Der `Hosting Validator` ist eine Minimal-Lösung zur Validierung von Hosting-Daten. Diese Lösung bietet eine UI-Demo und eine API-Schnittstelle.

## API-Schnittstelle
Die Schnittstelle kann von externen Systemen verwendet werden, um Hosting-Konfigurationen zu überprüfen. Senden Sie dazu einfach einen `POST`-Request an den Endpunkt.

### Endpoint
`POST /api/minimal-solutions/hosting_validator`

### Request-Beispiel
```json
{
  "source": "{\"host\": \"example.com\", \"ip\": \"192.168.1.1\"}",
  "config": "{}",
  "mode": "standard"
}
```

### Response-Beispiel
```json
{
  "success": true,
  "data": {
    "source": "{\"host\": \"example.com\", \"ip\": \"192.168.1.1\"}",
    "config": "{}",
    "mode": "standard",
    "validated_hosting": true,
    "message": "Hosting successfully validated."
  },
  "error": null,
  "warnings": [],
  "meta": {}
}
```
