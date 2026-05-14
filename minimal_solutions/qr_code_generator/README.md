# QR-Code Generator

## Overview
Minimal solution for generating QR codes. You can generate QR codes for different types of content, such as plain text, URLs, Wi-Fi credentials, or vCard contacts.

## API Endpoint
`/api/minimal-solutions/qr_code_generator`

## External Usage (API)
This API can be used externally by sending a `POST` request to the endpoint with a JSON payload containing the required parameters. The response will include a base64 encoded PNG image of the QR code.

**Request Example:**
```json
{
  "type": "url",
  "url": "https://example.com"
}
```

**Response Example:**
```json
{
  "status": "success",
  "data": {
    "type": "url",
    "format": "png",
    "size": 512,
    "url": "data:image/png;base64,iVBORw0KGgoAAA..."
  }
}
```

## UI Route
`/minimal-solutions/qr_code_generator`

## Tests
Tests for this solution follow the global test pattern:
- **Happy-Path**
- **Empty-Input**
- **Invalid-Input**
