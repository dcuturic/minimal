# Landingpage Formatter

The Landingpage Formatter is a minimal solution that provides an API and a UI to easily format landingpage structures based on a specific topic, target audience, and additional options.

## External Usage (API)

The tool exposes a REST API endpoint that allows external clients and systems to generate formatted landingpage data programmatically. It requires a JSON payload containing the configuration parameters and returns a structured JSON response.

### Endpoint
`POST /api/minimal-solutions/landingpage_formatter`

### Request Example
```json
{
  "topic": "Modern AI SaaS",
  "target": "Developers and Tech Founders",
  "options": "Dark mode, easy integration, low latency"
}
```

### Response Example
```json
{
  "status": "success",
  "data": {
    "formatted_landingpage": {
      "topic": "Modern AI SaaS",
      "target": "Developers and Tech Founders",
      "options": "Dark mode, easy integration, low latency",
      "generated_at": "2026-05-13T08:22:00Z"
    }
  }
}
```
