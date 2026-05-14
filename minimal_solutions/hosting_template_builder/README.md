# Hosting Template Builder

## Beschreibung
Der "Hosting Template Builder" ist eine Minimal-Lösung, die es ermöglicht, Konfigurationen und Parameter für Hosting-Umgebungen in Form von Templates aufzubereiten und zu bauen. Es stellt eine UI-Demo sowie eine API-Schnittstelle zur Verfügung.

## Verwendung der API

Die Lösung bietet einen API-Endpoint, der von externen Systemen aufgerufen werden kann.

**Endpoint:** `POST /api/minimal-solutions/hosting_template_builder`

Die Schnittstelle akzeptiert Anfragen im JSON-Format.

### Parameter
- `source` (Pflichtfeld): Ein String, der eine JSON-Repräsentation von Daten enthält (oder beliebigen anderen Text, den das Tool parst).
- `config` (Optional): Ein Dictionary (JSON-Objekt) oder JSON-String mit zusätzlichen Konfigurationsparametern für das Template.
- `mode` (Optional): Gibt den Verarbeitungsmodus an. Erlaubte Werte sind `default`, `strict` oder `verbose`. Fallback ist `default`.

### Request-Beispiel

```json
{
  "source": "{\"provider\": \"aws\", \"domain\": \"example.com\"}",
  "config": {
    "template_type": "docker",
    "region": "eu-central-1"
  },
  "mode": "strict"
}
```

### Response-Beispiel

```json
{
  "success": true,
  "data": {
    "source": "{\"provider\": \"aws\", \"domain\": \"example.com\"}",
    "config": {
      "template_type": "docker",
      "region": "eu-central-1"
    },
    "mode": "strict",
    "template_built": true,
    "status": "success",
    "message": "Template erfolgreich erstellt im Modus 'strict'."
  },
  "error": null,
  "warnings": [],
  "meta": {}
}
```

## Fehlerbehandlung
Die API verwendet das einheitliche globale Antwortformat. Im Fehlerfall (z. B. bei Validierungsfehlern) ist `success` auf `false` gesetzt, und das `error`-Objekt enthält weitere Details:

```json
{
  "success": false,
  "data": null,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Validierungsfehler",
    "details": {
      "source": "Dieses Feld wird benötigt."
    }
  },
  "warnings": [],
  "meta": {}
}
```
