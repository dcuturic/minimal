# Iframe Preview URL Builder

The Iframe Preview URL Builder is a minimal solution designed to generate iframe codes and preview URLs dynamically based on provided parameters such as page, component, and mode.

## API Usage

This solution provides a robust REST API endpoint that can be integrated externally to programmatically generate iframe embed codes and preview URLs.

### Endpoint

`POST /api/minimal-solutions/iframe_preview_url_builder`

### Parameters

At least `page` or `component` must be provided.

- `page` (string, optional): The target page name.
- `component` (string, optional): The target component name.
- `mode` (string, optional): The mode of the preview (e.g., "preview").

### Request Example

```json
{
  "page": "index",
  "component": "Header",
  "mode": "preview"
}
```

### Response Example

```json
{
  "status": "success",
  "data": {
    "preview_url": "/preview?page=index&component=Header&mode=preview",
    "iframe_code": "<iframe src=\"/preview?page=index&component=Header&mode=preview\" width=\"100%\" height=\"600px\" style=\"border: none; border-radius: 8px; overflow: hidden;\"></iframe>"
  }
}
```

## External Integration

You can easily use this endpoint in any external service or frontend application by making a standard HTTP POST request. Ensure the `Content-Type` is set to `application/json`. The resulting `iframe_code` can be directly injected into the DOM to render the preview frame safely.
