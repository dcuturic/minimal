# Robots TXT Generator

The **Robots TXT Generator** is a minimal solution on the CraftHoster platform that allows users to easily generate `robots.txt` files for their websites. It provides both a user-friendly UI and a direct API for generating rules for search engine crawlers.

## Features
- Set `User-agent` for the rules (defaults to `*` for all bots).
- Add multiple `Allow` paths to specify which directories are allowed.
- Add multiple `Disallow` paths to specify which directories are blocked.
- Automatically normalizes paths (e.g. adding leading slashes).
- Add an optional `Sitemap` URL.
- Accessible via Web UI and REST API.

## API Documentation

### Endpoint
`POST /api/minimal-solutions/robots_txt_generator`

### How to use the API externally
You can use this endpoint from any application (e.g. via cURL, Postman, or your frontend code). Send a JSON payload containing the required parameters (`user_agent`, `allow`, `disallow`, `sitemap_url`). The API will process the inputs and return a formatted `robots.txt` text block under the `data.result` field.

### Request Example (JSON)
```json
{
  "user_agent": "*",
  "allow": "/public/\n/assets/",
  "disallow": "/admin/\n/private/",
  "sitemap_url": "https://example.com/sitemap.xml"
}
```

### Response Example (JSON)
```json
{
  "status": "success",
  "data": {
    "result": "User-agent: *\nAllow: /public/\nAllow: /assets/\nDisallow: /admin/\nDisallow: /private/\nSitemap: https://example.com/sitemap.xml"
  }
}
```

### Integration
This solution is fully integrated into the CraftHoster standard architecture, including global error handling and validation logic.
