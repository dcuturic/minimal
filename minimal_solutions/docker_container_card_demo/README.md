# Docker Container Card Demo

Diese Minimal-Lösung bietet einen API-Endpunkt und ein UI-Element zur Generierung einer "Docker Container Card". Diese Card stellt den Status, den Namen, das Image und die Port-Konfiguration eines Docker-Containers visuell dar.

## API-Endpunkt

**Endpoint:** `POST /api/minimal-solutions/docker_container_card_demo`

**Request-Beispiel:**
```json
{
  "name": "web-server",
  "status": "running",
  "image": "nginx:latest",
  "ports": "80:80"
}
```

**Response-Beispiel:**
```json
{
  "status": "success",
  "data": {
    "name": "web-server",
    "status": "running",
    "image": "nginx:latest",
    "ports": "80:80",
    "timestamp": "2026-05-12T10:14:00Z"
  }
}
```

## UI / Integration

Die UI besteht aus einem Formular zur Eingabe von Container-Details (Name, Status, Image, Ports) und einer Vorschau-Ansicht (Preview-Box). In der Vorschau-Ansicht wird das Ergebnis in einem standardisierten, ansprechenden Container-Card-Format mit entsprechenden Status-Badges (z.B. Running, Stopped, Exited) dargestellt. 

Das generierte JSON kann zudem mit einem Klick in die Zwischenablage kopiert werden.
