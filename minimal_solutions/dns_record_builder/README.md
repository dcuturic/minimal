# DNS Record Builder

A tool to build and format DNS records.

## External API Usage
The interface uses the following endpoint:
`POST /api/minimal-solutions/dns_record_builder`

### Request Example
```json
{
  "type": "A",
  "name": "www",
  "value": "192.168.1.1",
  "ttl": 3600
}
```

### Response Example
```json
{
  "status": "success",
  "data": {
    "record": "www 3600 IN A 192.168.1.1",
    "type": "A",
    "name": "www",
    "value": "192.168.1.1",
    "ttl": 3600
  }
}
```
