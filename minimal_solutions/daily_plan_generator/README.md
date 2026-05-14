# Daily Plan Generator

Der Daily Plan Generator ist eine Minimal-Lösung, mit der du eine Liste von Aufgaben anhand einer vorgegebenen verfügbaren Stundenzahl zeitlich einteilen lassen kannst. Das Tool berechnet für jeden Task eine gleichmäßige Zeitspanne.

## API / Schnittstelle

Dieser Service kann extern als API genutzt werden, um programmgesteuert Aufgaben in einen tagesaktuellen, stundenbasierten Plan zu verteilen.

### Endpunkt
`POST /api/minimal-solutions/daily_plan_generator`

### Request-Beispiel
```json
{
  "tasks": [
    "Mails checken",
    "Meeting vorbereiten",
    "Ticket 123 bearbeiten"
  ],
  "available_hours": 8
}
```

### Response-Beispiel
```json
{
  "status": "success",
  "data": {
    "plan": [
      {
        "task": "Mails checken",
        "start_time": "09:00",
        "end_time": "11:40"
      },
      {
        "task": "Meeting vorbereiten",
        "start_time": "11:40",
        "end_time": "14:20"
      },
      {
        "task": "Ticket 123 bearbeiten",
        "start_time": "14:20",
        "end_time": "17:00"
      }
    ]
  }
}
```

## Validierung
- `tasks`: Muss eine nicht-leere Liste von Strings sein.
- `available_hours`: Muss eine Zahl (z.B. Float oder Integer) größer als 0 sein (und in der Regel maximal 24).
