# SLA Rechner

Ein Tool zur automatischen Berechnung von Service Level Agreement (SLA) Fristen basierend auf der Priorität und der Startzeit.

## Verwendung
Die API kann über einen POST-Request unter `/api/minimal-solutions/sla_rechner` angesprochen werden.

## API-Schnittstelle
- **Endpoint**: `POST /api/minimal-solutions/sla_rechner`
- **Content-Type**: `application/json`

### Request-Beispiel
```json
{
  "priority": "p1",
  "start_time": "2026-05-12T08:00:00"
}
```

### Response-Beispiel (Erfolg)
```json
{
  "success": true,
  "data": {
    "deadline": "2026-05-12 09:00",
    "priority_label": "P1 - Critical",
    "time_remaining": "1 Hours SLA"
  }
}
```

### Response-Beispiel (Fehler - z.B. Validierungsfehler)
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Validierungsfehler",
    "details": {
      "priority": "Unbekannte Priorität."
    }
  }
}
```

## Externe Verwendung
Die Schnittstelle kann problemlos von externen Diensten, wie beispielsweise einem Ticket-System, einem CRM oder einem Monitoring-Tool genutzt werden, um Fristen automatisch zu berechnen und SLAs zu überwachen. Ein einfacher HTTP-Client, wie `curl`, `fetch` in JavaScript oder `requests` in Python, reicht aus, um eine Anfrage an die API zu senden. Die Rückgabe erfolgt immer im strukturierten JSON-Format, wodurch die berechnete `deadline` und das `priority_label` direkt maschinell weiterverarbeitet werden können.
