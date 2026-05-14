# API Key Masker

The API Key Masker is a minimal solution that allows you to securely mask API keys or other secrets for display purposes, while keeping a specific number of characters visible at the start and end of the string.

## How to use the API

You can easily integrate the API Key Masker into your own applications by sending a `POST` request to our REST API endpoint.

**Endpoint:**
`POST /api/minimal-solutions/api_key_masker`

**Headers:**
- `Content-Type: application/json`

### Request Payload

The API expects a JSON body with the following fields:
- `secret` (string, required): The secret key you want to mask.
- `visible_start` (integer, optional, default: 0): The number of characters to leave visible at the beginning.
- `visible_end` (integer, optional, default: 0): The number of characters to leave visible at the end.

#### Example Request

```json
{
  "secret": "sk_live_1234567890abcdef",
  "visible_start": 4,
  "visible_end": 4
}
```

### Response

The API responds with a standard format containing a `status` and `data` object.

#### Example Response

```json
{
  "status": "success",
  "data": {
    "result": "sk_l****************cdef",
    "masked_key": "sk_l****************cdef"
  }
}
```

### Validation Errors
If you omit the `secret` or provide invalid types for the visible length parameters, the API will return a `400 Bad Request` or `422 Unprocessable Entity` with a detailed error message in the `details` field.
