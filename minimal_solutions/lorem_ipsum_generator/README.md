# Lorem Ipsum Generator

## Beschreibung
Der Lorem Ipsum Generator ist eine Minimal-Lösung zur einfachen Erstellung von Platzhaltertexten. Er bietet die Möglichkeit, Texte nach Absätzen, Wörtern, Bytes oder Listen zu generieren.

## Externe Nutzung (API)
Diese Lösung bietet eine API, die es ermöglicht, sie programmgesteuert von externen Systemen aus abzufragen. Die Schnittstelle akzeptiert POST-Anfragen und gibt strukturiertes JSON zurück.

### Endpunkt
`POST /api/minimal-solutions/lorem_ipsum_generator`

### Request-Format (JSON)
```json
{
  "mode": "paragraphs",
  "count": 2
}
```
Parameter:
- `mode`: Bestimmt das Format der Generierung (`paragraphs`, `words`, `bytes`, `lists`).
- `count`: Die Anzahl der zu generierenden Einheiten (Zahl zwischen 1 und 100).

### Response-Format (JSON)
```json
{
  "status": "success",
  "data": {
    "text": "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\nAt vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."
  }
}
```
