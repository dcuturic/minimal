# Cron Expression Helper

Der **Cron Expression Helper** ist eine Minimal-Lösung der CraftHoster Minimal Solutions Platform. Diese Lösung parst Cron-Ausdrücke, liefert eine menschenlesbare Beschreibung und berechnet die nächsten 5 Ausführungszeitpunkte.

## Externe Verwendung (API)

Die Schnittstelle kann problemlos von externen Services oder Scripts angesprochen werden. Sende hierfür einfach einen `POST`-Request im JSON-Format an unseren API-Endpunkt.

**Endpunkt:**
`POST /api/minimal-solutions/cron_expression_helper`

**Header:**
`Content-Type: application/json`

### Request-Beispiel

```json
{
  "cron_expression": "*/5 * * * *"
}
```

### Response-Beispiel (Erfolg)

```json
{
  "status": "success",
  "data": {
    "expression": "*/5 * * * *",
    "description": "Every 5 minutes",
    "next_executions": [
      "2026-05-11 13:00:00",
      "2026-05-11 13:05:00",
      "2026-05-11 13:10:00",
      "2026-05-11 13:15:00",
      "2026-05-11 13:20:00"
    ]
  }
}
```

### Response-Beispiel (Fehler)

```json
{
  "status": "error",
  "message": "Fehler beim Parsen des Cron-Ausdrucks: ..."
}
```
