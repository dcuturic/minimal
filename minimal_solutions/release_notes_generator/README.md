# Release Notes Generator

Minimal-Lösung für Release Notes Generator.

## API-Schnittstelle

Diese Minimal-Lösung bietet eine API zur automatischen Generierung von Release Notes im Markdown-Format. 
Die API kann von externen Diensten, CI/CD-Pipelines oder anderen Applikationen aufgerufen werden.

### Endpunkt
`POST /api/minimal-solutions/release_notes_generator`

### Request-Beispiel
```json
{
  "version": "2.1.0",
  "features": [
    "New dashboard widget", 
    "Support for dark mode"
  ],
  "fixes": [
    "Fixed login timeout issue"
  ],
  "breaking_changes": []
}
```

### Response-Beispiel
```json
{
  "status": "success",
  "data": {
    "result": "## Release Notes v2.1.0\n\n### Features\n- New dashboard widget\n- Support for dark mode\n\n### Fixes\n- Fixed login timeout issue\n"
  }
}
```
