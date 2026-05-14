# Docker Compose Service Viewer

Diese Minimal-Lösung analysiert `docker-compose.yml` Dateien und extrahiert die wichtigsten Service-Informationen.

## Features
- Parsing von Docker Compose YAML
- Extrahiert Service-Namen, Images, Ports und Volumes
- Bietet strukturierte Tabellenansicht in der UI
- API-Schnittstelle für externe Systeme

## UI
Erreichbar unter `/minimal-solutions/docker_compose_service_viewer`

## API

### Endpunkt
`POST /api/minimal-solutions/docker_compose_service_viewer`

### Request-Beispiel
```json
{
  "compose_yaml": "version: '3'\nservices:\n  web:\n    image: nginx\n    ports:\n      - \"80:80\""
}
```

### Response-Beispiel
```json
{
  "status": "success",
  "data": {
    "services": [
      {
        "name": "web",
        "image": "nginx",
        "ports": ["80:80"],
        "volumes": [],
        "build": null
      }
    ]
  }
}
```
