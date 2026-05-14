# vCard Generator

Ein einfaches Tool zur Generierung von elektronischen Visitenkarten (vCard/VCF-Format).

## API Schnittstelle

Die API kann über den Endpunkt `/api/minimal-solutions/vcard_generator` erreicht werden.

### Externe Verwendung

Sende einen POST-Request an den Endpunkt mit den Kontaktinformationen im JSON-Format. Die API gibt dann die fertige vCard als Text (String) zurück, zusammen mit den verarbeiteten Daten.

### Request

```json
{
  "name": "Max Mustermann",
  "email": "max@example.com",
  "phone": "+49 123 456789",
  "company": "Muster GmbH",
  "address": "Musterstraße 1\n12345 Musterstadt"
}
```

### Response

```json
{
  "status": "success",
  "data": {
    "vcard": "BEGIN:VCARD\r\nVERSION:3.0\r\nFN:Max Mustermann\r\nEMAIL:max@example.com\r\nTEL:+49 123 456789\r\nORG:Muster GmbH\r\nADR:;;Musterstraße 1\\n12345 Musterstadt;;;;\r\nEND:VCARD\r\n",
    "json": {
      "name": "Max Mustermann",
      "email": "max@example.com",
      "phone": "+49 123 456789",
      "company": "Muster GmbH",
      "address": "Musterstraße 1\n12345 Musterstadt"
    }
  }
}
```
