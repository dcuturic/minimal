# Subdomain Generator

A tool to generate subdomain suggestions based on a given name or keyword and a base domain.

## External API Usage
The interface uses the following endpoint:
`POST /api/minimal-solutions/subdomain_generator`

### Request Example
```json
{
  "name": "shop",
  "base_domain": "example.com"
}
```

### Response Example
```json
{
  "status": "success",
  "data": {
    "subdomains": [
      "shop.example.com",
      "my-shop.example.com",
      "get-shop.example.com",
      "shop-app.example.com"
    ]
  }
}
```
