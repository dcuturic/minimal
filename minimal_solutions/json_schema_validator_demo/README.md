# JSON Schema Validator Demo

The JSON Schema Validator is a minimal solution that allows you to validate any JSON data against a JSON Schema.

## Features
- Validate JSON against JSON Schema Draft-07.
- Detailed error messages if validation fails.
- Monochrome design matching the system style.
- API endpoint for external integrations.

## API Documentation

### Endpoint
`POST /api/minimal-solutions/json_schema_validator_demo`

### Description
Validates a given JSON object (`json_text`) against a provided JSON Schema (`schema_text`).

### Request Body Example
```json
{
  "json_text": {
    "name": "John Doe",
    "age": 30
  },
  "schema_text": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "name": { "type": "string" },
      "age": { "type": "integer", "minimum": 0 }
    },
    "required": ["name", "age"]
  }
}
```

### Response Example (Valid)
```json
{
  "status": "success",
  "message": "JSON Schema validated successfully",
  "data": {
    "is_valid": true,
    "errors": []
  }
}
```

### Response Example (Invalid)
```json
{
  "status": "success",
  "message": "JSON Schema validated successfully",
  "data": {
    "is_valid": false,
    "errors": [
      "'age' is a required property"
    ]
  }
}
```
