# Einheiten Converter

Ein Tool zur Konvertierung von Einheiten in den Kategorien Länge, Gewicht und Temperatur.

## Verwendung als API

Der Endpunkt ist unter `/api/minimal-solutions/einheiten_converter` erreichbar.

### Request Beispiel
```json
{
    "value": 100,
    "from_unit": "km",
    "to_unit": "m",
    "category": "length"
}
```

### Response Beispiel
```json
{
    "status": "success",
    "data": {
        "result": 100000.0,
        "formatted": "100000.0 m"
    }
}
```
