# API Request Builder Minimal Solution

This is a minimal solution for building and previewing API requests. It supports common HTTP methods (GET, POST, PUT, PATCH, DELETE) and allows you to construct requests with custom headers and JSON bodies.

## API Endpoint

**URL:** `/api/minimal-solutions/api_request_builder`
**Method:** `POST`

## How to Use Externally

You can use this endpoint in external applications by making an HTTP POST request. You must provide the `method` and `url` parameters. The `headers` and `body` parameters are optional depending on the HTTP method chosen.

### Request Example

```json
{
  "method": "POST",
  "url": "https://api.example.com/v1/users",
  "headers": {
    "Authorization": "Bearer token",
    "Content-Type": "application/json"
  },
  "body": {
    "name": "John Doe",
    "email": "john@example.com"
  }
}
```

### Response Example

```json
{
  "status": "success",
  "data": {
    "preview": "POST /v1/users HTTP/1.1\nHost: api.example.com\nAuthorization: Bearer token\nContent-Type: application/json\n\n{\n  \"name\": \"John Doe\",\n  \"email\": \"john@example.com\"\n}",
    "method": "POST",
    "url": "https://api.example.com/v1/users",
    "headers": {
      "Authorization": "Bearer token",
      "Content-Type": "application/json"
    },
    "body": {
      "name": "John Doe",
      "email": "john@example.com"
    }
  }
}
```

## Validation Rules

- `method`: String. Must be one of: 'GET', 'POST', 'PUT', 'PATCH', 'DELETE'. Defaults to 'GET'.
- `url`: String. Must be a valid URL starting with http:// or https://. Required.
- `headers`: Dictionary. Optional. Must be a valid JSON object.
- `body`: Any valid JSON (Dictionary, List, String, Number, Boolean, Null). Optional. Only permitted for POST, PUT, PATCH, DELETE methods.
