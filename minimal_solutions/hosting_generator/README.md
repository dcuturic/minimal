# Hosting Generator

Diese Minimal-Lösung ermöglicht die Erstellung von Hosting-Konfigurationen (wie Dockerfiles oder Nginx-Configs) basierend auf einer Quellcode-URL und einem gewünschten Hosting-Modus.

## Externe Nutzung (API)

Die Funktionalität steht über eine API-Schnittstelle zur Verfügung und kann von externen Systemen aufgerufen werden.

### Endpunkt

`POST /api/minimal-solutions/hosting_generator`

### Parameter

- `source` (String, Pflicht): Quellcode-Repository oder Verzeichnis.
- `mode` (String, Pflicht): Die Hosting-Umgebung (z.B. docker, static, nodejs).
- `config` (Object, Optional): Zusätzliche Parameter als JSON.

### Request-Beispiel

```json
{
  "source": "https://github.com/example/repo",
  "mode": "docker",
  "config": {
    "port": 8080,
    "env": "production"
  }
}
```

### Response-Beispiel

```json
{
  "status": "success",
  "data": {
    "dockerfile": "FROM node:18\n...",
    "commands": [
      "docker build -t app .",
      "docker run -p 8080:8080 app"
    ],
    "environment": "production"
  }
}
```
