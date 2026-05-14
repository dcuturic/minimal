# UUID Generator

Minimal solution for generating UUIDs.

## External API Usage

The UUID Generator provides a RESTful JSON API that can be used from external services.

### Endpoint
`POST /api/minimal-solutions/uuid_generator`

### Request Format
Send a JSON payload with the `Content-Type: application/json` header.
- `count` (integer): Number of UUIDs to generate (1-100). Default is 1.
- `version` (integer): UUID version (1, 3, 4, or 5). Version 4 (random) is default.

Example Request:
```json
{
  "count": 3,
  "version": 4
}
```

### Response Format
Returns a JSON object with the generated UUIDs.
```json
{
  "status": "success",
  "data": {
    "uuids": [
      "e4ea61d1-671c-4b61-9c60-a241eb405786",
      "2b7e1516-28aec-4660-8f9d-11445b23d932",
      "a30f14d9-81a1-4357-bb03-68f760db1e9f"
    ],
    "count": 3,
    "version": 4
  }
}
```
