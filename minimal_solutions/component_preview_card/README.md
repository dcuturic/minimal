# Component Preview Card

A minimal solution for generating a standardized preview card wrapper around raw HTML components.

## API Usage

You can interact with this service externally via the following API endpoint:
`POST /api/minimal-solutions/component_preview_card`

### Request Example
```json
{
  "component_name": "Primary Button",
  "category": "UI Elements",
  "preview_html": "<button class=\"btn btn-primary\">Click Me</button>"
}
```

### Response Example
```json
{
  "status": "success",
  "data": {
    "component_name": "Primary Button",
    "category": "UI Elements",
    "generated_card_html": "<div class=\"cpc-result-header\">...</div><div class=\"cpc-result-body\"><button class=\"btn btn-primary\">Click Me</button></div>"
  }
}
```

### Description

Send a JSON payload with `component_name`, `category` and the raw `preview_html` to receive a wrapped HTML string that applies the standard platform design and layouts around your component.
