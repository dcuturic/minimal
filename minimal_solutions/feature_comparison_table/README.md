# Feature Comparison Table

The **Feature Comparison Table** minimal solution provides a dynamic way to compare features across multiple items (e.g., pricing plans, products, software versions). It offers a user interface for generating comparison tables and copying the results as HTML, or downloading them as JSON. It also exposes a REST API for programmatic access.

## API Usage

The API allows you to send a list of features and items, and it will return a formatted JSON object that is ready to be consumed by your application or frontend to render a comparison table.

### Endpoint

**POST** `/api/minimal-solutions/feature_comparison_table`

### Request Example

```json
{
  "features": [
    "Storage",
    "Users",
    "Support"
  ],
  "items": [
    {
      "name": "Basic",
      "values": {
        "Storage": "10 GB",
        "Users": "1",
        "Support": "Email"
      }
    },
    {
      "name": "Pro",
      "values": {
        "Storage": "100 GB",
        "Users": "5",
        "Support": "Priority"
      }
    }
  ]
}
```

### Response Example

```json
{
  "status": "success",
  "data": {
    "features": [
      "Storage",
      "Users",
      "Support"
    ],
    "items": [
      {
        "name": "Basic",
        "values": {
          "Storage": "10 GB",
          "Users": "1",
          "Support": "Email"
        }
      },
      {
        "name": "Pro",
        "values": {
          "Storage": "100 GB",
          "Users": "5",
          "Support": "Priority"
        }
      }
    ]
  }
}
```

### Error Handling

If validation fails (e.g., missing fields or incorrect data types), the API returns a structured error response:

```json
{
  "status": "error",
  "message": "Items are required.",
  "code": "VALIDATION_ERROR"
}
```
