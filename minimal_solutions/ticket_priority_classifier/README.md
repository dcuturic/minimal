# Ticket Priority Classifier

Diese Minimal-Lösung bietet eine einfache und schnelle Möglichkeit, Kunden-Tickets anhand ihres Textes zu analysieren und eine Dringlichkeitsstufe (Priority) zuzuweisen.

## Externe API-Nutzung

Die Schnittstelle kann problemlos von externen Diensten (z.B. einem anderen Backend, einem Ticket-System wie Jira/Zendesk oder einer Automatisierungs-Pipeline) angebunden werden. Hierfür steht ein REST-API-Endpunkt zur Verfügung, der JSON-Daten akzeptiert und als Antwort strukturiertes JSON zurückgibt.

**Endpunkt:**
`POST /api/minimal-solutions/ticket_priority_classifier`

**Header:**
`Content-Type: application/json`

### Request-Beispiel

```json
{
  "ticket_text": "The entire server is down and clients are complaining. Fix immediately!"
}
```

### Response-Beispiel

```json
{
  "status": "success",
  "data": {
    "priority": "Urgent",
    "confidence": 0.98,
    "reason": "Contains terms like 'server is down', 'clients complaining', 'immediately'."
  }
}
```

## UI-Komponente
Die Lösung verfügt zudem über eine dynamische UI-Komponente, die das Testen der Klassifizierung direkt im Browser ermöglicht. Inklusive einer API-Doku-Box für Entwickler.
