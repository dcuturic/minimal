# Component JSON Builder

A minimal solution for building unified Component JSONs from standard web parts like template, env data, css, and js.

## API Usage
You can interact with this service via the following endpoint:
`POST /api/minimal-solutions/component_json_builder`

### Request Example
```json
{
  "template": "<div class=\"my-component\">\n  Hello {{ name }}\n</div>",
  "env": { "name": "World" },
  "css": ".my-component { color: red; }",
  "js": "console.log('Component initialized');"
}
```

### Response Example
```json
{
  "status": "success",
  "data": {
    "template": "<div class=\"my-component\">\n  Hello {{ name }}\n</div>",
    "env": { "name": "World" },
    "css": ".my-component { color: red; }",
    "js": "console.log('Component initialized');"
  }
}
```

The API expects JSON data with a mandatory `template` string. The other fields (`env`, `css`, `js`) are optional but will be validated if provided.
