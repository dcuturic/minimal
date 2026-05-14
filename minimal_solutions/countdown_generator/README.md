# Countdown Generator

Minimal-Lösung für einen Countdown Generator.

## Übersicht
Der Countdown Generator berechnet die verbleibende Zeit (in Tagen, Stunden, Minuten und Sekunden) bis zu einem bestimmten Zieldatum. Er kann in verschiedenen Anwendungen genutzt werden, um Spannung für Events, Launches oder Deadlines aufzubauen.

## API-Nutzung
Die Minimal-Lösung ist als REST-API verfügbar. Sende Anfragen im JSON-Format an den Endpunkt.

**Endpunkt:**
`POST /api/minimal-solutions/countdown_generator`

### Request-Beispiel (JSON)
```json
{
  "target_date": "2027-01-01T00:00:00",
  "label": "Neujahr"
}
```

### Response-Beispiel (JSON)
```json
{
  "status": "success",
  "data": {
    "title": "Neujahr",
    "days": 234,
    "hours": 5,
    "minutes": 34,
    "seconds": 8
  }
}
```

## Integration
Die Lösung kann einfach in andere Anwendungen integriert werden, indem Anfragen an die API gesendet werden. Für eine anschauliche Visualisierung steht die Demo-Seite (UI) zur Verfügung.
