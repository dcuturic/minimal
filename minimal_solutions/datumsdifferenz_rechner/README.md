# Datumsdifferenz Rechner

Berechnet die Differenz zwischen zwei Daten in Jahren, Monaten, Tagen und gibt Gesamtsummen für Tage, Wochen und Monate aus.

## Externe Verwendung (API)

Die Minimal-Lösung bietet eine REST-API-Schnittstelle, die extern angesprochen werden kann.

**Endpunkt:**
`POST /api/minimal-solutions/datumsdifferenz_rechner`

### Request-Beispiel

Die API erwartet einen JSON-Body mit den Parametern `start_date` und `end_date` im ISO-Format (`YYYY-MM-DD`):

```javascript
fetch('/api/minimal-solutions/datumsdifferenz_rechner', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
        "start_date": "2023-01-01",
        "end_date": "2023-12-31"
    })
});
```

### Response-Beispiel

Die Antwort enthält die berechneten Differenz-Statistiken:

```json
{
    "status": "success",
    "data": {
        "years": 0,
        "months": 11,
        "days": 30,
        "total_days": 364,
        "total_weeks": 52,
        "total_months": 11
    }
}
```
