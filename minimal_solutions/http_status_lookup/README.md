# HTTP Status Lookup

A minimal tool to lookup HTTP status codes and display their message and description.

## Usage
Send a POST request to `/api/minimal-solutions/http_status_lookup` with a `status_code` integer.

## API Endpoint
`POST /api/minimal-solutions/http_status_lookup`

### Request Example
```json
{
  "status_code": 404
}
```

### Response Example
```json
{
  "status": "success",
  "data": {
    "status_code": 404,
    "message": "Not Found",
    "description": "The server can not find the requested resource. In the browser, this means the URL is not recognized."
  }
}
```
