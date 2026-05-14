# SEO Analyzer

Minimal solution for SEO Analysis.

## API Usage

The SEO Analyzer functionality can be accessed externally via its API.

### Endpoint
`POST /api/minimal-solutions/seo_analyzer`

### Request Example
```json
{
  "topic": "https://example.com",
  "target": "Desktop",
  "options": ["check_density"]
}
```

### Response Example
```json
{
  "status": "success",
  "data": {
    "score": 85,
    "issues": [],
    "keyword_density": "2.5%"
  }
}
```
