# SWOT Generator

Dies ist die Minimal-Lösung für einen **SWOT Generator**.

## Beschreibung
Der SWOT Generator generiert basierend auf einem Thema und optionalen Notizen eine strukturierte SWOT-Analyse.

## Externe Verwendung der API

Die Schnittstelle kann problemlos von externen Systemen (wie eigenen Backends, Automatisierungstools wie n8n, Make oder Zapier) verwendet werden, um SWOT-Daten in bestehende Prozesse zu integrieren. 
Senden Sie dazu einfach einen POST-Request an den unten stehenden Endpunkt mit den entsprechenden JSON-Parametern im Body.

**Endpunkt:**
`POST /api/minimal-solutions/swot_generator`

**Header:**
`Content-Type: application/json`

**Request-Beispiel:**
```json
{
  "topic": "Launching a new e-commerce platform",
  "notes": "Budget is limited, but we have a strong team."
}
```

**Response-Beispiel:**
```json
{
  "status": "success",
  "data": {
    "strengths": ["Strong marketing team"],
    "weaknesses": ["Limited budget"],
    "opportunities": ["Growing market"],
    "threats": ["Established competitors"]
  }
}
```
