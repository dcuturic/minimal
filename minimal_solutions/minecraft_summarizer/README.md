# Minecraft Summarizer

Der Minecraft Summarizer ist eine Minimal-Lösung zur Zusammenfassung und Analyse von Minecraft-Daten (z. B. Logs, Konfigurationen).

## Externe Nutzung (API)

Die Funktion steht als API-Schnittstelle zur Verfügung und kann von externen Systemen über einen `POST`-Request genutzt werden.

### Endpoint
`POST /api/minimal-solutions/minecraft_summarizer`

### Header
- `Content-Type: application/json`

### Request-Body
Die Schnittstelle erwartet ein JSON-Objekt mit folgenden Feldern:
- `input_text` (String, Pflichtfeld): Der zu verarbeitende Text (z.B. Log-Dateien oder Konfigurationen).
- `mode` (String, Optional): Der Verarbeitungsmodus (Standard: `summarize`). Mögliche Werte sind `summarize`, `bulletpoints`, `extract_errors`.
- `options` (Object, Optional): Zusätzliche Parameter für die Verarbeitung.

**Request-Beispiel:**
```json
{
  "input_text": "Lange server.properties oder log content...",
  "options": {
    "length": "short"
  },
  "mode": "summarize"
}
```

### Response
Die API antwortet im standardisierten globalen Format. Im Erfolgsfall ist `success: true` und die Ergebnisse finden sich im `data` Objekt unter `summarizer_output`.

**Response-Beispiel:**
```json
{
  "success": true,
  "data": {
    "input_text": "Lange server.properties oder log content...",
    "options": {
      "length": "short"
    },
    "mode": "summarize",
    "summarizer_output": "Zusammengefasster Text...",
    "status": "success",
    "message": "Minecraft Summarizer erfolgreich ausgefuehrt."
  },
  "error": null,
  "warnings": [],
  "meta": {}
}
```

### UI Demo
Die Minimal-Lösung bietet zudem eine grafische Benutzeroberfläche zur schnellen manuellen Validierung. Dort ist ebenfalls die API-Doku hinterlegt, um Beispiele direkt per Copy-Paste nutzen zu können.
