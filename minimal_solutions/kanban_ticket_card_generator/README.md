# Kanban Ticket Card Generator

The Kanban Ticket Card Generator is a minimal solution that provides a clean UI and API to generate styled HTML cards for Kanban-style tickets.

## External Usage (API)

The generator can be integrated into external systems (like task managers or CLI tools) via our REST API. You can programmatically generate HTML card representations of tickets by sending a POST request to the API endpoint with the ticket details.

### Endpoint

`POST /api/minimal-solutions/kanban_ticket_card_generator`

### Request Example

```json
{
  "title": "Fix Navigation Bug",
  "description": "Navigation is broken on mobile",
  "priority": "high",
  "status": "todo"
}
```

### Response Example

```json
{
  "status": "success",
  "data": {
    "card": {
      "title": "Fix Navigation Bug",
      "description": "Navigation is broken on mobile",
      "priority": "high",
      "status": "todo"
    },
    "html_preview": "<div class=\"ktcg-card\">...</div>"
  }
}
```
