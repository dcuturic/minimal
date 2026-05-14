# Theme Token Editor Demo

Minimal solution for editing theme tokens.

## Description
This solution provides a user interface to visually edit and preview theme color tokens. It accepts a JSON input containing color tokens and provides a visual editor to change their values. Once edited, the updated JSON can be easily copied.

## API Integration

This minimal solution provides an API endpoint that can be used externally to validate and parse theme tokens.

**Endpoint:** `POST /api/minimal-solutions/theme_token_editor_demo`

**Content-Type:** `application/json`

### Request Example
```json
{
  "tokens": {
    "primary": "#00ffcc",
    "background": "#121212"
  }
}
```

### Response Example (Success)
```json
{
  "status": "success",
  "data": {
    "tokens": {
      "primary": "#00ffcc",
      "background": "#121212"
    }
  }
}
```

### Usage
Externally, you can send a POST request with the tokens payload to this API endpoint to ensure the token format is valid before applying it to your application's theme configuration.
