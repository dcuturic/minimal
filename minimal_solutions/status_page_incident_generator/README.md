# Status Page Incident Generator

This solution generates a standardized status page incident update based on the affected service, incident type, current status, and message.

## API Usage

The service exposes a POST endpoint: `/api/minimal-solutions/status_page_incident_generator`

### Request Example
```json
{
  "service": "Core Platform",
  "incident_type": "Outage",
  "status": "Investigating",
  "message": "We are currently investigating reports of connectivity issues affecting the Core Platform."
}
```

### Response Example
```json
{
  "status": "success",
  "data": {
    "result": {
      "incident": {
        "service": "Core Platform",
        "incident_type": "Outage",
        "status": "Investigating",
        "message": "We are currently investigating reports of connectivity issues affecting the Core Platform.",
        "created_at": "2026-05-12T14:19:14Z",
        "id": "inc_1234567890"
      },
      "formatted_text": "[2026-05-12T14:19:14Z] INCIDENT - CORE PLATFORM (INVESTIGATING)\nType: Outage\nMessage: We are currently investigating reports of connectivity issues affecting the Core Platform."
    }
  }
}
```

### External Usage

To use this interface externally, send a POST request with a JSON body to the endpoint. The application must supply valid strings for all fields. The response will contain both a structured `incident` object and a `formatted_text` string which can be used to quickly copy-paste into communication channels.
