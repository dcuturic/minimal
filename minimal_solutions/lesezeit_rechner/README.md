# Lesezeit Rechner

## Übersicht
Der **Lesezeit Rechner** berechnet die geschätzte Lesezeit für einen beliebigen Text basierend auf der Lesegeschwindigkeit (Wörter pro Minute).

## UI-Integration
Die Benutzeroberfläche ist unter `/minimal-solutions/lesezeit_rechner` erreichbar und fügt sich nahtlos in das globale monochrome Design der CraftHoster Plattform ein.

## API-Nutzung
Diese Minimal-Lösung kann einfach in externe Anwendungen integriert werden.

**Endpoint:**
`POST /api/minimal-solutions/lesezeit_rechner`

**Request-Beispiel (JSON):**
```json
{
  "text": "Dies ist ein Beispieltext, um die Lesezeit zu berechnen.",
  "words_per_minute": 200
}
```

**Response-Beispiel (JSON):**
```json
{
  "status": "success",
  "data": {
    "result": "0 sek",
    "minutes": 0,
    "seconds": 3,
    "total_seconds": 3,
    "word_count": 9
  }
}
```
