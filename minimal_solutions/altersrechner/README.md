# Altersrechner

Ein Tool zur Berechnung des Alters basierend auf einem Geburtsdatum und einem optionalen Zieldatum (standardmäßig das heutige Datum).

## Verwendung als API

Der Endpunkt ist unter `/api/minimal-solutions/altersrechner` erreichbar.

### Request Beispiel
```json
{
    "birth_date": "1990-05-15",
    "target_date": "2026-05-11"
}
```
`target_date` ist optional. Wenn nicht angegeben, wird das aktuelle Datum verwendet.

### Response Beispiel
```json
{
    "status": "success",
    "data": {
        "years": 35,
        "months": 11,
        "days": 26,
        "total_days": 13145,
        "total_weeks": 1877,
        "total_months": 431
    }
}
```
