# Minecraft Analyzer

Der **Minecraft Analyzer** ist eine Minimal-Lösung zur Analyse von Minecraft-Daten. Er bietet sowohl eine Benutzeroberfläche (UI) als auch eine API-Schnittstelle.

## Externe Verwendung der Schnittstelle

Die API kann von externen Systemen über einen `POST`-Request aufgerufen werden. Die Anfrage muss im JSON-Format gesendet werden und die Parameter `input_text`, `mode` und `options` enthalten.

**Endpoint:**
`POST /api/minimal-solutions/minecraft_analyzer`

### Request-Beispiel

```json
{
  "input_text": "server.properties content...",
  "options": {"verbose": true},
  "mode": "analyze"
}
```

### Response-Beispiel

```json
{
  "success": true,
  "data": {
    "input_text": "server.properties content...",
    "options": {
      "verbose": true
    },
    "mode": "analyze",
    "analyzer_output": "...",
    "status": "success",
    "message": "Minecraft Analyzer erfolgreich ausgefuehrt."
  },
  "error": null,
  "warnings": [],
  "meta": {}
}
```
