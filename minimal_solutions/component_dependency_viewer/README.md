# Component Dependency Viewer

Eine Minimal-Lösung, die die Abhängigkeiten einer UI-Komponente auswertet und als Liste anzeigt.

## API-Schnittstelle

Diese Lösung bietet eine REST-API-Schnittstelle zur externen Nutzung an.
Senden Sie einen POST-Request an den entsprechenden Endpunkt mit den erforderlichen Daten im JSON-Format.

### Endpunkt

`POST /api/minimal-solutions/component_dependency_viewer`

### Request-Beispiel

```json
{
  "component_json": {
    "name": "MyComponent",
    "dependencies": ["Button", "Icon"]
  }
}
```

### Response-Beispiel

```json
{
  "status": "success",
  "data": {
    "dependencies": ["Button", "Icon"]
  }
}
```
