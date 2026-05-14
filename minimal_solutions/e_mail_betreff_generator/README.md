# E-Mail Betreff Generator

## Beschreibung
Der E-Mail Betreff Generator erstellt ansprechende und klickstarke Betreffzeilen für E-Mail-Kampagnen. Er berücksichtigt Thema, Zielgruppe und Tonalität.

## Externe Nutzung der API
Die Schnittstelle kann extern über HTTP POST Requests genutzt werden, um automatisiert E-Mail-Betreffzeilen in eigenen Anwendungen (z.B. Newsletter-Software, CRM) zu generieren.

### Endpoint
`POST /api/minimal-solutions/e_mail_betreff_generator`

### Request Body (JSON)
```json
{
    "topic": "Black Friday Sale",
    "audience": "Bestandskunden",
    "tone": "urgent"
}
```

### Response (JSON)
```json
{
    "status": "success",
    "data": {
        "subjects": [
            "🚨 Black Friday: Exklusiv für Bestandskunden",
            "Nur heute: VIP-Sale für dich",
            "Dein Early-Access: Black Friday"
        ]
    }
}
```
