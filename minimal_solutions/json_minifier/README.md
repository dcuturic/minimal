# JSON Minifier

Minimal-Lösung: JSON Minifier.

## Overview
The JSON Minifier is a tool to compress and minify JSON strings by removing unnecessary whitespace and formatting. This reduces payload size for faster transmission over networks and saves storage space.

## External Usage (API)
This solution can be accessed programmatically via its API endpoint. By sending a POST request to the endpoint with the `json_text` property, you will receive the fully minified JSON format.

### Endpoint
`POST /api/minimal-solutions/json_minifier`

### Request Example
```json
{
  "json_text": "{\n  \"example\": \"data\"\n}"
}
```

### Response Example
```json
{
  "status": "success",
  "data": {
    "minified_json": "{\"example\":\"data\"}",
    "original_size_bytes": 22,
    "minified_size_bytes": 18,
    "saved_percentage": 18.18
  }
}
```
