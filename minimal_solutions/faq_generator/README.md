# FAQ Generator

## Übersicht
Der **FAQ Generator** ist eine Minimal-Lösung, die es ermöglicht, automatisch häufig gestellte Fragen (FAQs) und deren Antworten aus einem bereitgestellten Text zu generieren. 

## Externe Nutzung (API)
Diese Funktion kann auch programmgesteuert über eine REST-API-Schnittstelle aufgerufen werden. Dies ist nützlich, um die FAQ-Generierung in externe Systeme oder Workflows einzubinden.

### API Endpoint
**POST** `/api/minimal-solutions/faq_generator`

### Request-Beispiel
Der Request muss als `application/json` gesendet werden und ein Feld `source_text` (String) enthalten, sowie optional ein `count` (Integer).
```json
{
  "source_text": "Our new service offers 24/7 support and unlimited bandwidth. It costs $9.99 per month. You can cancel anytime.",
  "count": 3
}
```

### Response-Beispiel
Bei einem erfolgreichen Aufruf liefert der Endpunkt die generierten Fragen und Antworten im Feld `faqs` unterhalb von `data` zurück.
```json
{
  "status": "success",
  "data": {
    "faqs": [
      {
        "question": "What kind of support is available?",
        "answer": "We offer 24/7 support."
      },
      {
        "question": "How much does the service cost?",
        "answer": "The service costs $9.99 per month."
      },
      {
        "question": "Can I cancel my subscription?",
        "answer": "Yes, you can cancel anytime."
      }
    ]
  }
}
```

### Fehlerbehandlung
Falls Parameter fehlen oder ungültig sind, antwortet die API mit entsprechenden Error-Codes:
- `400 Bad Request`: Wenn die Eingabe kein gültiges JSON ist.
- `422 Unprocessable Entity`: Wenn z. B. `source_text` fehlt oder leer ist, oder wenn `count` kein Integer oder außerhalb des gültigen Bereichs ist.
- `500 Internal Server Error`: Bei unerwarteten internen Verarbeitungsfehlern.
