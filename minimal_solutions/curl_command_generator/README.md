# cURL Command Generator

Eine Minimal-Lösung, die aus HTTP-Methoden, URLs, Headern und einem Body einen fertigen `curl`-Befehl generiert.

## Verwendung (Extern über API)

Die API kann problemlos von externen Diensten angesprochen werden, um programmatisch cURL-Befehle zu generieren. 
Sende dazu einfach einen `POST`-Request mit einem JSON-Payload an den Endpunkt.

**Endpunkt:**  
`POST /api/minimal-solutions/curl_command_generator`

### Request-Beispiel
```json
{
  "method": "POST",
  "url": "https://api.example.com/v1/users",
  "headers": {
    "Authorization": "Bearer token",
    "Content-Type": "application/json"
  },
  "body": {
    "name": "John Doe",
    "email": "john@example.com"
  }
}
```

### Response-Beispiel
```json
{
  "status": "success",
  "data": {
    "curl_command": "curl -X POST https://api.example.com/v1/users \\\n  -H 'Authorization: Bearer token' \\\n  -H 'Content-Type: application/json' \\\n  -d '{\"name\": \"John Doe\", \"email\": \"john@example.com\"}'"
  }
}
```
