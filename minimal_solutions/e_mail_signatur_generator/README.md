# E-Mail Signatur Generator

Dieser Service generiert eine professionelle HTML-Signatur für E-Mails auf Basis der übergebenen Benutzerdaten.

## Externe Verwendung (API)

Die Schnittstelle kann extern über eine HTTP-POST-Anfrage aufgerufen werden. Du übergibst ein JSON-Objekt mit den gewünschten Daten und erhältst ein JSON-Objekt mit dem generierten HTML-Code zurück. Dieser HTML-Code kann dann direkt in E-Mail-Clients oder Anwendungen eingefügt werden.

### Endpunkt
`POST /api/minimal-solutions/e_mail_signatur_generator`

### Request-Beispiel
```json
{
  "name": "Max Mustermann",
  "role": "Software Engineer",
  "company": "CraftHoster",
  "email": "max@example.com",
  "phone": "+49 123 456789",
  "website": "https://crafthoster.de"
}
```

### Response-Beispiel
```json
{
  "status": "success",
  "data": {
    "signature_html": "<div style=\"font-family: Arial, sans-serif; font-size: 14px; color: #333333;\"><strong>Max Mustermann</strong><br><span>Software Engineer | CraftHoster</span><br><br><span>E-Mail: <a href=\"mailto:max@example.com\" style=\"color: #0056b3;\">max@example.com</a></span><br><span>Telefon: +49 123 456789</span><br><span>Website: <a href=\"https://crafthoster.de\" style=\"color: #0056b3;\">https://crafthoster.de</a></span></div>"
  }
}
```

### Parameter
- **name** (String, erforderlich): Der Name der Person.
- **role** (String, optional): Die Position oder Rolle der Person.
- **company** (String, optional): Der Name des Unternehmens.
- **email** (String, erforderlich): Die E-Mail-Adresse. Muss eine gültige E-Mail-Adresse sein.
- **phone** (String, optional): Die Telefonnummer.
- **website** (String, optional): Die Website oder URL des Unternehmens/der Person.
