# Hosting Analyzer

Der Hosting Analyzer ist ein Tool, das Hosting-Daten analysiert und validiert. Diese Minimal-Lösung bietet sowohl eine Benutzeroberfläche zur direkten Nutzung als auch eine REST-API-Schnittstelle.

## Externe Nutzung der API-Schnittstelle

Die API kann von externen Systemen aufgerufen werden, um automatisierte Hosting-Analysen durchzuführen. Hierfür muss ein HTTP `POST`-Request an den entsprechenden Endpoint gesendet werden. Die Eingabedaten (Source, Config, Mode) werden im JSON-Format im Request-Body übergeben.

**Endpoint:** `POST /api/minimal-solutions/hosting_analyzer`

### Request-Beispiel

```json
{
  "source": "example.com\nexample.net",
  "config": "{\"verbose\": true}",
  "mode": "analyze"
}
```

### Response-Beispiel

```json
{
  "success": true,
  "data": {
    "status": "success",
    "message": "Hosting analysis completed successfully.",
    "analysis_results": {
      "domain_count": 2,
      "mode_used": "analyze",
      "issues_found": 0,
      "recommendations": [
        "Optimize DNS settings",
        "Check SSL certificates"
      ]
    }
  },
  "error": null,
  "warnings": [],
  "meta": {}
}
```
