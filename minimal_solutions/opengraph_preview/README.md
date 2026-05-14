# OpenGraph Preview

Minimal solution for OpenGraph Preview.

## API Usage

The OpenGraph Preview API allows external applications to generate OpenGraph preview data programmatically.

### Endpoint
`POST /api/minimal-solutions/opengraph_preview`

### Request Example
```json
{
  "title": "My Awesome Website",
  "description": "This is an awesome website about cool things.",
  "image_url": "https://example.com/image.png",
  "domain": "example.com"
}
```

### Response Example
```json
{
  "status": "success",
  "data": {
    "title": "My Awesome Website",
    "description": "This is an awesome website about cool things.",
    "image_url": "https://example.com/image.png",
    "domain": "example.com"
  }
}
```
