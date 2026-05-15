# Minecraft Merger

Minimal-Lösung 'Minecraft Merger'.

## Beschreibung
Dieses Modul bietet Funktionalitäten für das Mergen von Minecraft-Daten. Es nimmt eine Liste von Texten entgegen und verbindet diese basierend auf dem gewählten Modus und den Optionen.

## Externe Verwendung der API
Die Schnittstelle kann von externen Anwendungen über einen einfachen HTTP POST Request angesprochen werden. Der Request-Body muss als JSON formatiert sein und den Header `Content-Type: application/json` enthalten.

### Endpunkt
- **URL**: `/api/minimal-solutions/minecraft_merger`
- **Methode**: `POST`

### Request-Beispiel
```json
{
  "input_text": ["Steve", "diamond", "64"],
  "mode": "basic",
  "options": {
    "join_character": ":"
  }
}
```

### Response-Beispiel
Bei erfolgreicher Verarbeitung liefert die API folgende Struktur zurück:
```json
{
  "success": true,
  "data": {
    "merged_result": "Steve:diamond:64",
    "mode": "basic",
    "timestamp": "2024-05-14T12:00:00Z"
  }
}
```

Im Fehlerfall (z.B. bei ungültigen Eingaben):
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Validation failed",
    "details": {
      "mode": ["Mode is required."]
    }
  }
}
```
