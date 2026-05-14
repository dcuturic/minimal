# Hosting Builder

Minimal-Lösung für das Starten eines Hosting-Builds.

## API Endpunkt

`POST /api/minimal-solutions/hosting_builder`

Dieser Endpunkt nimmt Hosting-Details (Quellpfad, Konfiguration, Build-Modus) entgegen und startet simuliert einen Build-Prozess.

### Externe Verwendung

Die Schnittstelle kann extern per HTTP POST-Request aufgerufen werden.

**Request-Beispiel (cURL):**
```bash
curl -X POST http://localhost:8000/api/minimal-solutions/hosting_builder \
  -H "Content-Type: application/json" \
  -d '{
    "source": "github.com/user/repo",
    "mode": "standard",
    "config": {
      "branch": "main",
      "env": "prod",
      "install_deps": true
    }
  }'
```

**Response-Beispiel:**
```json
{
  "status": "success",
  "data": {
    "build_id": "bld_123456789",
    "status": "building",
    "source": "github.com/user/repo",
    "mode": "standard"
  }
}
```
