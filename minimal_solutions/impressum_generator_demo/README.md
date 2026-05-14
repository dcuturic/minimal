# Impressum Generator Demo

Dies ist eine Minimal-Lösung für einen Impressum Generator.
Sie kann über die Benutzeroberfläche oder programmgesteuert als externe API verwendet werden.

## API-Nutzung

Die Schnittstelle kann extern verwendet werden, um ein Impressum basierend auf Unternehmensdaten automatisch zu generieren.

### Endpunkt

`POST /api/minimal-solutions/impressum_generator_demo`

### Request-Beispiel

```json
{
  "company": "Muster GmbH",
  "address": "Musterstraße 1, 12345 Musterstadt",
  "email": "info@mustergmbh.de",
  "phone": "+49 123 456789",
  "representative": "Max Mustermann"
}
```

### Response-Beispiel

```json
{
  "status": "success",
  "data": {
    "impressum_text": "Impressum\n\nMuster GmbH\nMusterstraße 1, 12345 Musterstadt\n\nVertreten durch:\nMax Mustermann\n\nKontakt:\nTelefon: +49 123 456789\nE-Mail: info@mustergmbh.de"
  }
}
```
