# Kontaktkarten Generator

Ein Tool zum Erstellen von vCards und JSON-Kontaktkarten aus einfachen Formulardaten.

## API Schnittstelle

Die API kann über den Endpunkt `/api/minimal-solutions/kontaktkarten_generator` erreicht werden.

### Request
```json
{
  "name": "Max Mustermann",
  "email": "max@example.com",
  "phone": "+49 123 456789",
  "company": "Musterfirma GmbH",
  "website": "https://example.com"
}
```

### Response
```json
{
  "status": "success",
  "data": {
    "vcard": "BEGIN:VCARD\r\nVERSION:3.0\r\nFN:Max Mustermann\r\nORG:Musterfirma GmbH\r\nTEL:+49 123 456789\r\nEMAIL:max@example.com\r\nURL:https://example.com\r\nEND:VCARD",
    "json": {
      "name": "Max Mustermann",
      "email": "max@example.com",
      "phone": "+49 123 456789",
      "company": "Musterfirma GmbH",
      "website": "https://example.com"
    }
  }
}
```

### Externe Nutzung
Du kannst die API in eigenen Projekten nutzen, indem du einen POST-Request mit den entsprechenden Daten sendest. Das System validiert die Eingabe (mindestens `name` ist erforderlich) und liefert im Erfolgsfall sofort die formatierte vCard als Text, sowie eine strukturierte JSON-Repräsentation zurück.
