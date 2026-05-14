# ENV File Viewer

Minimal solution for parsing and viewing environment variables from `.env` files while securely separating keys and values.

## Externe Nutzung (API)

Die Funktionalität des ENV File Viewers kann auch über eine externe API-Schnittstelle genutzt werden. Senden Sie dazu einen POST-Request an den entsprechenden Endpunkt.

**Endpoint:** `POST /api/minimal-solutions/env_file_viewer`

**Request Headers:**
- `Content-Type: application/json`

**Request Body Beispiel:**
```json
{
  "env_text": "DB_HOST=localhost\nDB_PASSWORD=secret123\nAPI_KEY=sk_live_abc123"
}
```

**Response Beispiel:**
```json
{
  "status": "success",
  "data": {
    "env_vars": [
      {
        "key": "DB_HOST",
        "value": "localhost"
      },
      {
        "key": "DB_PASSWORD",
        "value": "secret123"
      },
      {
        "key": "API_KEY",
        "value": "sk_live_abc123"
      }
    ]
  }
}
```
