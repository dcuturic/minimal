# Hosting Preview

Dies ist die Minimal-Lösung für "Hosting Preview". Sie bietet eine Schnittstelle, um eine Live-Vorschau einer Hosting-Konfiguration zu generieren.

## Externe Verwendung der API

Die Schnittstelle kann von externen Diensten (wie z.B. CI/CD-Pipelines oder anderen Microservices) aufgerufen werden, um Hosting-Vorschauen auszulösen. Sende dazu einen HTTP `POST`-Request mit dem Header `Content-Type: application/json` an den unten stehenden Endpunkt.

### API Endpunkt
`POST /api/minimal-solutions/hosting_preview`

### Request (Beispiel)

Erwartet wird ein JSON-Body. Das Feld `source` ist zwingend erforderlich, `config` und `mode` sind optional.

```json
{
  "source": "github.com/user/repo",
  "config": {
    "branch": "main",
    "env": "prod"
  },
  "mode": "standard"
}
```

### Response (Beispiel)

Die API antwortet gemäß dem globalen Response-Standard. Im Erfolgsfall wird der HTTP-Status `200 OK` zurückgegeben.

```json
{
  "status": "success",
  "data": {
    "preview_url": "https://preview-1234.hosting.app",
    "deployment_id": "dep_9876abc",
    "status": "ready",
    "source": "github.com/user/repo",
    "mode": "standard"
  }
}
```

## Dateien in diesem Modul
- `ui_hosting_preview.html`: Das User Interface.
- `api_hosting_preview.py`: Der API-Endpunkt.
- `validation_hosting_preview.py`: Validierungslogik für den Endpunkt.
- `test_hosting_preview.py`: Tests.
- `demo_hosting_preview.json`: Beispieldaten.
