# Sitemap XML Generator

A minimal solution to generate a valid `sitemap.xml` snippet based on given URLs.

## Features
- Enter one or more URLs.
- Select the `changefreq` (e.g. daily, weekly).
- Set a `priority` value (0.0 to 1.0).
- Validates the input and ensures a well-formed XML structure output.

## External API Usage

The interface can be used programmatically via a RESTful API.

### Endpoint
`POST /api/minimal-solutions/sitemap_xml_generator`

### Headers
`Content-Type: application/json`

### Request Example
```json
{
  "urls": [
    "https://example.com/",
    "https://example.com/about/"
  ],
  "changefreq": "daily",
  "priority": 0.5
}
```

### Response Example
```json
{
  "status": "success",
  "data": {
    "sitemap_xml": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n  <url>\n    <loc>https://example.com/</loc>\n    <changefreq>daily</changefreq>\n    <priority>0.5</priority>\n  </url>\n  <url>\n    <loc>https://example.com/about/</loc>\n    <changefreq>daily</changefreq>\n    <priority>0.5</priority>\n  </url>\n</urlset>"
  }
}
```

The response includes the `status` and `data` objects, matching the platform's standard API structure. You can integrate this anywhere where automated sitemap generation is needed.
