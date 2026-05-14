# Decision Log Generator

Ein minimales Tool zum Erstellen von formatierten Entscheidungs-Logs (Decision Logs) auf Basis von Kontext, Entscheidung und Begründung.

## API-Nutzung (Externer Aufruf)

Die Funktionalität kann extern über eine REST-Schnittstelle aufgerufen werden. 

**Endpoint:** `POST /api/minimal-solutions/decision_log_generator`
**Content-Type:** `application/json`

### Request-Beispiel
```json
{
  "context": "We need to choose a database for the new platform...",
  "decision": "PostgreSQL",
  "reason": "It provides strong relational integrity and JSONB support."
}
```

### Response-Beispiel
```json
{
  "status": "success",
  "data": {
    "decision_log": "### Decision Log\n\n**Context:**\nWe need to choose a database for the new platform...\n\n**Decision:**\nPostgreSQL\n\n**Reason:**\nIt provides strong relational integrity and JSONB support."
  }
}
```
