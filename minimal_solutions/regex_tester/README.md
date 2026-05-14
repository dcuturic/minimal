# Regex Tester Minimal-Lösung

## Übersicht
Der Regex Tester ist eine Minimal-Lösung, mit der reguläre Ausdrücke (RegEx) direkt im Browser gegen Testtexte geprüft werden können. Die Lösung bietet visuelles Highlighting für Matches und zeigt Detailinformationen (Treffermenge und Match-Positionen) an.

## API-Nutzung (Extern)
Die Funktion ist auch als REST-API verfügbar und kann von externen Applikationen genutzt werden, um serverseitig Regex-Tests und Auswertungen durchzuführen.

**Endpoint:** `POST /api/minimal-solutions/regex_tester`

### Request (JSON)
```json
{
  "pattern": "^[a-z]+$",
  "flags": "i",
  "text": "Hello World"
}
```

- `pattern`: Der reguläre Ausdruck als String (z.B. `^[0-9]+$`). Muss valide sein.
- `text`: Der zu durchsuchende Test-Text.
- `flags` (optional): RegEx Flags wie `i` (Ignore Case), `m` (Multiline), `s` (DotAll).

### Response (Erfolg)
```json
{
  "status": "success",
  "data": {
    "matches": [
      {
        "match": "Hello",
        "start": 0,
        "end": 5,
        "groups": []
      },
      {
        "match": "World",
        "start": 6,
        "end": 11,
        "groups": []
      }
    ],
    "count": 2
  }
}
```

### Response (Fehler)
```json
{
  "status": "error",
  "code": "BAD_REQUEST",
  "message": "Ungültiger Regex: missing ), unterminated subpattern at position 3"
}
```
