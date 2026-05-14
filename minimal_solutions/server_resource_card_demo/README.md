# Server Resource Card Demo

A minimal solution to generate server resource dashboard cards based on given CPU, RAM, and Disk metrics. This component is part of the CraftHoster Minimal Solutions Platform.

## Externally Accessible API

The service offers a REST API endpoint that can be utilized to generate dashboard metrics externally. It receives CPU, RAM, and Disk values and returns them in a standard format.

**Endpoint**: `POST /api/minimal-solutions/server_resource_card_demo`

### Request Example
```json
{
  "cpu": 45.5,
  "ram": 78.2,
  "disk": 92.0
}
```

### Response Example
```json
{
  "status": "success",
  "data": {
    "cpu": 45.5,
    "ram": 78.2,
    "disk": 92.0,
    "timestamp": "2026-05-12T09:50:36Z"
  }
}
```
