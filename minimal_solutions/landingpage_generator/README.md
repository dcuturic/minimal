# Landingpage Generator

This minimal solution provides a tool to generate structured landingpage data (headlines, subheadlines, features) based on a topic, target audience, and optional features.

## API Usage

The tool exposes a REST API endpoint that allows external applications to programmatically generate landingpage content.

### Endpoint

`POST /api/minimal-solutions/landingpage_generator`

### Request Header

`Content-Type: application/json`

### Request Body Example

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
    "landingpage_data": {
      "headline": "Empower your Development with AI",
      "subheadline": "Low latency tools designed for Tech Founders.",
      "features": [
        "Dark Mode",
        "Easy Integration",
        "Low Latency"
      ]
    }
  }
}
```
