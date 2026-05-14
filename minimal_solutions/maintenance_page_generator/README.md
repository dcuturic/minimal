# Maintenance Page Generator

A minimal solution to generate a beautifully styled, simple HTML maintenance page.

## API Usage

The service exposes a POST endpoint: `/api/minimal-solutions/maintenance_page_generator`

This interface can be used externally to generate maintenance pages programmatically before deploying them to a web server, reverse proxy, or load balancer.

### Request Example
```json
{
  "title": "Under Maintenance",
  "message": "We are currently performing scheduled maintenance. We will be back online shortly.",
  "eta": "2 Hours"
}
```

### Response Example
```json
{
  "status": "success",
  "data": {
    "html_output": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n..."
  }
}
```
