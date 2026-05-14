# Language Key Editor Demo

A minimal solution to generate a multi-language translation editor from a list of keys and languages.

## API Integration

**Endpoint**: `POST /api/minimal-solutions/language_key_editor_demo`

### Request Example
```json
{
  "keys": [
    "login.title",
    "login.submit"
  ],
  "languages": [
    "en",
    "de"
  ]
}
```

### Response Example
```json
{
  "status": "success",
  "data": {
    "translations": {
      "login.title": {
        "en": "",
        "de": ""
      },
      "login.submit": {
        "en": "",
        "de": ""
      }
    }
  }
}
```

## How to use externally

Send a `POST` request to the endpoint with the JSON payload containing `keys` and `languages` arrays. The API will respond with an initialized translation structure that you can use to map keys to empty string values for the given languages.
