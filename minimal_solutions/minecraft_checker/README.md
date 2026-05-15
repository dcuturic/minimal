# Minecraft Checker API

Diese Minimal-Lösung bietet eine Schnittstelle zur Überprüfung von Minecraft-Daten (z. B. Server-Status, Spieler-Namen). 

## Verwendung

Die Schnittstelle kann von externen Systemen aufgerufen werden, indem ein `POST`-Request mit den entsprechenden Parametern als JSON-Body gesendet wird.

### API Endpoint

`POST /api/minimal-solutions/minecraft_checker`

### Request-Format (JSON)

- `input_text` (String, required): Der zu überprüfende Text oder die Adresse.
- `mode` (String, required): Der Modus für die Prüfung (z.B. `check`, `verify`, `ping`).
- `options` (Object, optional): Optionale Konfigurationen für die Ausführung.

#### Request-Beispiel

```json
{
  "input_text": "mc.example.com",
  "mode": "check",
  "options": {
    "verbose": true
  }
}
```

### Response-Format

Die API gibt ein standardisiertes JSON-Objekt zurück, in dem `data` das Ergebnis der Überprüfung enthält.

#### Response-Beispiel

```json
{
  "success": true,
  "data": {
    "input_text": "mc.example.com",
    "mode": "check",
    "options": {
      "verbose": true
    },
    "status": "success",
    "message": "Minecraft Checker request successfully processed for mode 'check'.",
    "result": {
      "check_status": "passed",
      "issues_found": 0,
      "details": "Checked 'mc.example.com...' in mode 'check'. No issues found."
    }
  },
  "error": null,
  "warnings": [],
  "meta": {}
}
```
