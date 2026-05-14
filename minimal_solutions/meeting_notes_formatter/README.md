# Meeting Notes Formatter API

Dieser Service bietet einen API-Endpunkt, um unstrukturierte Meeting-Notizen oder Textblöcke automatisch in strukturierte Formate und Action Items umzuwandeln. Ideal zur Integration in Slack-Bots, CRM-Systeme oder interne Tools.

## Endpunkt

`POST /api/minimal-solutions/meeting_notes_formatter`

## Request Payload (JSON)

Die API erwartet ein JSON-Objekt mit folgendem Feld:

- `notes` (string, erforderlich): Der unstrukturierte Text oder die rohen Notizen. Darf nicht leer sein.

### Request-Beispiel

```json
{
  "notes": "team sync. talked about budget and q3 goals. anna will prepare the presentation by friday. budget approved for 50k. need to call the agency."
}
```

## Response (JSON)

Die API antwortet standardisiert. Bei Erfolg enthält das `data`-Objekt die Felder `formatted_notes` (strukturierte Punkte) und `action_items` (gefundene Aufgaben/To-Dos).

### Erfolgs-Response

```json
{
  "status": "success",
  "data": {
    "formatted_notes": "- Team Sync.\n- Talked about budget and Q3 goals.\n- Budget approved for 50k.",
    "action_items": [
      "Anna will prepare the presentation by friday.",
      "Need to call the agency."
    ]
  }
}
```

### Fehler-Response (Beispiel: Fehlendes `notes`-Feld)

```json
{
  "status": "error",
  "message": "Validation failed",
  "errors": {
    "notes": "Das Feld 'notes' ist erforderlich."
  }
}
```

## Fehlerbehandlung

- Wenn `notes` fehlt, kein String ist oder leer ist, wird der Statuscode `400 Bad Request` zurückgegeben und die Fehler werden im `errors`-Objekt detailliert.
- Bei internen Verarbeitungsfehlern (z.B. AI-Service nicht erreichbar) wird eine generische Fehlermeldung mit Statuscode `500` oder `400` zurückgegeben.
