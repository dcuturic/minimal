# Task Breakdown Generator

Eine Minimal-Lösung, die es ermöglicht, eine textuelle Aufgabenbeschreibung (`task_text`) sowie eine gewünschte Granularität (`depth`) in eine formatierte Liste von Unter-Aufgaben (Tickets) herunterzubrechen. Ideal für Projektmanagement, Kanban-Boards und die Strukturierung von größeren Arbeitspaketen.

## API-Nutzung

Diese Lösung kann über eine REST API angesprochen werden.

**Endpoint:** `POST /api/minimal-solutions/task_breakdown_generator`

### Request-Beispiel

```json
{
  "task_text": "Build a simple login page",
  "depth": 2
}
```

### Response-Beispiel

```json
{
  "status": "success",
  "data": {
    "tickets": [
      {
        "title": "Create User Login UI",
        "description": "Design and build the login form with email and password fields."
      },
      {
        "title": "Implement Login API",
        "description": "Create the backend endpoint to handle authentication."
      }
    ]
  }
}
```

### Externe Verwendung
Die API kann von externen Applikationen (z.B. Task-Trackern, CI/CD-Pipelines oder CLI-Tools) aufgerufen werden, indem ein `POST`-Request mit dem Content-Type `application/json` an den obigen Endpoint gesendet wird. Dies erlaubt die nahtlose Integration der Task-Aufschlüsselungslogik in andere Arbeitsabläufe.
