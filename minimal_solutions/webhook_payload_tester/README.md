# Webhook Payload Tester

A minimal solution to validate and pretty-print JSON webhook payloads.

## Overview

The Webhook Payload Tester allows users to paste raw JSON webhook payloads, validates their format, and displays a pretty-printed, syntax-highlighted version of the parsed data. It is useful for quickly checking the structure and validity of incoming webhooks from external services.

## API Integration

You can use the Webhook Payload Tester programmatically via its API endpoint.

**Endpoint:** `POST /api/minimal-solutions/webhook_payload_tester`

**Content-Type:** `application/json`

### Request Example

```json
{
  "payload_json": "{\n  \"event\": \"user.created\",\n  \"data\": {\n    \"user_id\": \"123\"\n  }\n}"
}
```

### Response Example

```json
{
  "status": "success",
  "data": {
    "is_valid": true,
    "message": "The webhook payload is valid and correctly formatted.",
    "parsed_payload": {
      "event": "user.created",
      "data": {
        "user_id": "123"
      }
    }
  }
}
```
