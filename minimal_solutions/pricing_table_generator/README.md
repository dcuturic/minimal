# Pricing Table Generator

Eine Minimal-Lösung für die Generierung von responsiven, modernen Pricing Tabellen (Preistabellen). 

## API / Schnittstelle

Dieses Modul kann extern als API genutzt werden, um Pricing-Pläne strukturiert als JSON zu übergeben und als standardisierte Antwort zurückzuerhalten. Dies ist nützlich für die Validierung oder für andere Applikationen, die diese Datenstruktur benötigen.

**Endpunkt:**
`POST /api/minimal-solutions/pricing_table_generator`

### Request-Beispiel
```json
{
  "plans": [
    {
      "name": "Basic",
      "price": "9",
      "currency": "$",
      "period": "/mo",
      "features": ["1 User", "5GB Storage"],
      "is_popular": false,
      "button_text": "Get Started"
    }
  ]
}
```

### Response-Beispiel
```json
{
  "status": "success",
  "data": {
    "result": [
      {
        "name": "Basic",
        "price": "9",
        "currency": "$",
        "period": "/mo",
        "features": ["1 User", "5GB Storage"],
        "is_popular": false,
        "button_text": "Get Started"
      }
    ]
  }
}
```
