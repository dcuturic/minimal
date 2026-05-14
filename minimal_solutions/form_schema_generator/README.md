# Form Schema Generator

The **Form Schema Generator** is a minimal solution that allows you to easily generate JSON Schemas by defining an array of field properties.

## External Usage / API Integration

You can use the Form Schema Generator programmatically via our API.

### Endpoint

`POST /api/minimal-solutions/form_schema_generator`

### Request Format

Send a JSON payload with a `fields` array. Each field should define its `name`, `type`, and whether it is `required`.

```json
{
  "fields": [
    {
      "name": "username",
      "type": "string",
      "required": true
    },
    {
      "name": "age",
      "type": "integer",
      "required": false
    }
  ]
}
```

### Response Format

The API will return a JSON object with a `status` and `data` containing the generated `schema`.

```json
{
  "status": "success",
  "data": {
    "schema": {
      "type": "object",
      "properties": {
        "username": {
          "type": "string"
        },
        "age": {
          "type": "integer"
        }
      },
      "required": [
        "username"
      ]
    }
  }
}
```
