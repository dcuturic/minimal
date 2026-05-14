# Access Role Matrix Demo

This minimal solution generates a visual access role matrix based on a list of roles and permissions.

## UI

The UI allows users to input multiple roles and permissions, and visually generates a matrix table showing the relationships between them. It is designed following the global monochrome design system.

## API Integration

The tool provides an API endpoint that evaluates the roles and permissions and returns a structured matrix.

**Endpoint:** `POST /api/minimal-solutions/access_role_matrix_demo`

### Request Example
```json
{
  "roles": ["Admin", "Editor", "Viewer"],
  "permissions": ["read", "write", "delete"]
}
```

### Response Example
```json
{
  "status": "success",
  "data": {
    "matrix": [
      {
        "role": "Admin",
        "permissions": {
          "read": true,
          "write": true,
          "delete": true
        }
      },
      {
        "role": "Editor",
        "permissions": {
          "read": true,
          "write": true,
          "delete": false
        }
      },
      {
        "role": "Viewer",
        "permissions": {
          "read": true,
          "write": false,
          "delete": false
        }
      }
    ]
  }
}
```
