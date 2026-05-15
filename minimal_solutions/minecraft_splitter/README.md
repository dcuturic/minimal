# Minecraft Splitter

Minimal-Lösung für den Minecraft Splitter.

## Beschreibung
Dieses Tool bietet Funktionen, um Minecraft-Daten (z. B. Inventar-Strings, Befehle, Koordinaten) basierend auf verschiedenen Modi und spezifischen Trennzeichen strukturiert in einzelne Bestandteile aufzuteilen ("zu splitten").

## Externe Nutzung der Schnittstelle (API)
Dieser Service kann extern als REST-API genutzt werden, um Daten automatisiert aufzuteilen. Senden Sie dazu einfach einen `POST`-Request mit den erforderlichen Parametern (`input_text`, `mode`, `options`) im JSON-Format an den unten stehenden Endpunkt. Das System validiert die Eingaben und liefert die gesplitteten Daten strukturiert als JSON zurück.

## API-Endpunkt
`POST /api/minimal-solutions/minecraft_splitter`

### Request-Beispiel
```json
{
  "input_text": "Steve:diamond:64",
  "mode": "basic",
  "options": {
    "split_character": ":"
  }
}
```

### Response-Beispiel
```json
{
  "success": true,
  "data": {
    "split_result": [
      "Steve",
      "diamond",
      "64"
    ],
    "mode": "basic",
    "timestamp": "2024-05-14T12:00:00Z"
  }
}
```
