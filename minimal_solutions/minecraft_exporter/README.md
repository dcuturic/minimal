# Minecraft Exporter

Der **Minecraft Exporter** ist eine Minimal-Lösung zum Exportieren, Extrahieren und Konvertieren von Minecraft-Daten (z. B. Logs, JSON-Daten, Inventar) über eine REST-Schnittstelle.

## Externe Verwendung (API)

Die Schnittstelle kann von externen Systemen aufgerufen werden, indem ein `POST`-Request mit den entsprechenden Parametern als JSON-Body gesendet wird.

### Endpoint
`POST /api/minimal-solutions/minecraft_exporter`

### Parameter (JSON Body)
- `input_text` (String, Pflicht): Die Minecraft-Eingabedaten (z. B. JSON-Daten).
- `mode` (String, Optional): Verarbeitungsmodus. Erlaubte Werte: `export`, `extract`, `convert`. Standardwert ist `export`.
- `options` (Object, Optional): Weitere Optionen als JSON-Objekt. Z. B. `{"format": "csv"}`.

### Request-Beispiel
```bash
curl -X POST http://localhost:5000/api/minimal-solutions/minecraft_exporter \
-H "Content-Type: application/json" \
-d '{
  "input_text": "{\"player\": \"Steve\", \"score\": 100}",
  "mode": "export",
  "options": {"format": "csv"}
}'
```

### Response-Beispiel
```json
{
  "success": true,
  "data": {
    "input_text": "{\"player\": \"Steve\", \"score\": 100}",
    "mode": "export",
    "options": {
      "format": "csv"
    },
    "status": "success",
    "message": "Minecraft Exporter request successfully processed for mode 'export'.",
    "result": {
      "exported_data": "player,score\nSteve,100"
    }
  },
  "error": null,
  "warnings": [],
  "meta": {}
}
```
