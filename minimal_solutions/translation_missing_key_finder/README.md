# Translation Missing Key Finder

A minimal solution for identifying missing translation keys between a base JSON (source of truth) and a target JSON.

## API Usage
You can interact with this service via the following endpoint:
`POST /api/minimal-solutions/translation_missing_key_finder`

### External Usage
You can use this API in CI/CD pipelines or translation management scripts to automatically detect missing keys in your language files before deploying. Send the base and target JSON payloads via a POST request and parse the `missing_keys` array in the response.

### Request Example
```json
{
  "base_json": {
    "welcome": "Welcome",
    "nav": {
      "home": "Home",
      "about": "About"
    }
  },
  "target_json": {
    "welcome": "Willkommen",
    "nav": {
      "home": "Startseite"
    }
  }
}
```

### Response Example
```json
{
  "status": "success",
  "data": {
    "missing_keys": [
      "nav.about"
    ]
  }
}
```
