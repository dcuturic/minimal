# SEO Mapper

Der **SEO Mapper** ist eine Minimal-Lösung zum Mappen von SEO-Daten basierend auf einem spezifischen Topic und Target.

## Externe Nutzung als API

Die Funktionalität des SEO Mappers kann über eine REST-API-Schnittstelle von externen Applikationen angesprochen werden.

### Endpunkt

`POST /api/minimal-solutions/seo_mapper`

### Request-Beispiel

```json
{
  "topic": "Content Marketing",
  "target": "increase_traffic",
  "options": "fast_mode"
}
```

### Response-Beispiel

```json
{
  "status": "success",
  "data": {
    "topic": "Content Marketing",
    "target": "increase_traffic",
    "mapped_status": "success",
    "message": "Daten für 'Content Marketing' erfolgreich gemappt."
  }
}
```

### Parameter

- **topic** (String, erforderlich): Das primäre Keyword oder Thema.
- **target** (String, erforderlich): Das Ziel, z. B. "increase_traffic" oder "lead_generation".
- **options** (String, optional): Zusätzliche Parameter oder Modi für die Verarbeitung.

### Integration

Sende einen `POST` Request mit dem Content-Type `application/json` an den Endpunkt. Bei Erfolg (`status: "success"`) erhältst du die gemappten Daten im `data` Objekt zurück. Im Fehlerfall wird ein Fehler-Status sowie eine entsprechende Fehlermeldung ausgegeben.
