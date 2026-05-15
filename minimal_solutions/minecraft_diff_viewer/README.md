# Minecraft Diff Viewer

Die Minimal-Lösung 'Minecraft Diff Viewer' bietet eine Schnittstelle, um Minecraft-Daten (z. B. Arrays oder Objekte) basierend auf verschiedenen Modi miteinander zu vergleichen (diff).

## Externe Nutzung der Schnittstelle (API)

Der Service kann problemlos als externe API angesprochen werden.

### Endpunkt
`POST /api/minimal-solutions/minecraft_diff_viewer`

### Request-Format
Die API erwartet ein JSON-Objekt mit den folgenden Feldern:
- `input_text` (Array oder Object): Die zu vergleichenden Daten.
- `mode` (String): Der Modus, z.B. "diff".
- `options` (Object): Zusätzliche Optionen wie z.B. `{"strict_mode": true}`.

**Beispiel-Request:**
```json
{
  "input_text": [{"name": "Diamond Sword"}, {"name": "Iron Sword"}],
  "mode": "diff",
  "options": {
    "strict_mode": true
  }
}
```

### Response-Format
Die API gibt ein JSON-Objekt mit dem Resultat zurück.

**Beispiel-Response:**
```json
{
  "success": true,
  "data": {
    "diff_result": [
      {"name": "Diamond Sword"},
      {"name": "Iron Sword"}
    ],
    "mode": "diff",
    "options": {
      "strict_mode": true
    },
    "message": "Diff erfolgreich durchgeführt."
  }
}
```

## UI Route

Für Entwickler- und Testzwecke steht eine Benutzeroberfläche zur Verfügung:
`GET /minimal-solutions/minecraft_diff_viewer/demo`
