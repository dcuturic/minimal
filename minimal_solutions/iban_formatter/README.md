# IBAN Formatter

Eine Minimal-Lösung, die eine eingegebene IBAN bereinigt, im offiziellen Format (mit Leerzeichen alle 4 Zeichen) zurückgibt und eine grundlegende Formatvalidierung durchführt.

## Verwendung (Extern)
Die Schnittstelle kann extern per REST-API angesprochen werden, um IBANs programmgesteuert zu formatieren und zu validieren.

**Endpoint:** `POST /api/minimal-solutions/iban_formatter`

**Content-Type:** `application/json`

### Request-Beispiel
```json
{
  "iban": "de89370400440532013000"
}
```

### Response-Beispiel (Erfolgreich)
```json
{
  "status": "success",
  "data": {
    "iban": "DE89370400440532013000",
    "formatted_iban": "DE89 3704 0044 0532 0130 00",
    "is_valid": true
  }
}
```

### Response-Beispiel (Fehler - Validierung)
```json
{
  "status": "error",
  "message": "Validierungsfehler",
  "code": "VALIDATION_ERROR",
  "details": [
    {
      "field": "iban",
      "issue": "Das Feld 'iban' darf nicht leer sein."
    }
  ]
}
```
