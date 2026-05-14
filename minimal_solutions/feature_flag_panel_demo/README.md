# Feature Flag Panel Demo

Eine Minimal-Lösung zur einfachen Verwaltung von Feature Flags. Aus einer einfachen Liste von Feature-Namen wird ein dynamisches UI-Panel generiert, über das Features als Toggles (Ein/Aus) dargestellt werden. 

## Externe Nutzung (API)

Diese Minimal-Lösung bietet auch eine Schnittstelle (API), die extern genutzt werden kann, um Feature Flags zu validieren und in ein strukturiertes JSON-Format umzuwandeln. Die Schnittstelle kann von anderen Diensten oder Frontends aufgerufen werden.

### Endpunkt

`POST /api/minimal-solutions/feature_flag_panel_demo`

### Request-Beispiel

```json
{
  "flags": [
    "enable_new_dashboard",
    "beta_search_v2",
    "experimental_dark_mode"
  ]
}
```

### Response-Beispiel

```json
{
  "status": "success",
  "data": {
    "flags": [
      {
        "name": "enable_new_dashboard",
        "enabled": false
      },
      {
        "name": "beta_search_v2",
        "enabled": false
      },
      {
        "name": "experimental_dark_mode",
        "enabled": false
      }
    ]
  }
}
```
