# SSL Expiry Checker Demo

A tool to check the SSL certificate expiry details for a given domain.

## External API Usage
The interface uses the following endpoint:
`POST /api/minimal-solutions/ssl_expiry_checker_demo`

### Request Example
```json
{
  "domain": "google.com"
}
```

### Response Example
```json
{
  "status": "success",
  "data": {
    "domain": "google.com",
    "is_valid": true,
    "days_remaining": 65,
    "expiry_date": "2026-07-16T12:00:00.000Z",
    "issuer": {
      "commonName": "GTS CA 1C3",
      "organizationName": "Google Trust Services LLC",
      "countryName": "US"
    }
  }
}
```

This REST API can be integrated into external services to monitor domain certificate validity and proactively alert on upcoming expirations.
