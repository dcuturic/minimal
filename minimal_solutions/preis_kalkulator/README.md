# Preis Kalkulator

Eine Minimal-Lösung zur Berechnung von Margen, Rabatten, Aufschlägen und dem finalen Endpreis auf Basis eines Grundpreises.

## API Nutzung

Die Lösung kann als externe API in eigenen Systemen oder Applikationen verwendet werden.

**Endpoint:** `POST /api/minimal-solutions/preis_kalkulator`

### Request Beispiel

```json
{
  "base_price": 100.0,
  "margin": 10.0,
  "discount": 5.0,
  "markup": 2.5
}
```

### Response Beispiel

```json
{
  "status": "success",
  "data": {
    "base_price": 100.0,
    "margin_amount": 10.0,
    "discount_amount": 5.0,
    "markup_amount": 2.5,
    "final_price": 107.5
  }
}
```

### Extern Verwenden
Die API-Schnittstelle akzeptiert einen POST-Request mit dem Content-Type `application/json`.
Dadurch lässt sich der Preis Kalkulator einfach und nahtlos in Webshops, Rechnungstools, ERP-Systeme oder interne Dashboards integrieren.
