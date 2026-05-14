# Landingpage Cleaner

Die Minimal-Lösung "Landingpage Cleaner" ist ein Tool zur Bereinigung und Formatierung von Landingpage-Daten. Es kann über die UI verwendet werden oder als API-Schnittstelle in externe Anwendungen integriert werden.

## API-Schnittstelle extern verwenden

Dieser Service bietet einen REST-API-Endpunkt, um die Landingpage-Bereinigung programmgesteuert durchzuführen. 

**Endpunkt:**  
`POST /api/minimal-solutions/landingpage_cleaner`

**Content-Type:**  
`application/json`

### Request-Beispiel

```json
{
  "topic": "Produkt-Launch",
  "target": "Neukunden",
  "options": {
    "remove_duplicates": true,
    "trim_spaces": true
  }
}
```

### Response-Beispiel

```json
{
  "status": "success",
  "data": {
    "topic": "Produkt-Launch",
    "target": "Neukunden",
    "options": {
      "remove_duplicates": true,
      "trim_spaces": true
    },
    "clean_id": "cln_123456",
    "timestamp": "2026-05-13T12:00:00Z",
    "cleaned": true
  }
}
```

Durch das Senden eines POST-Requests an die URL der API kann das Tool automatisch Eingabedaten für Landingpages formatieren, verarbeiten und aufbereitet zurückgeben. Fehlerhafte oder fehlende Eingaben werden über den `status: "error"` im Response-JSON kommuniziert.
