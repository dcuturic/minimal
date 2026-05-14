# AI Agent Instruction Builder

Die "AI Agent Instruction Builder" Minimal-Lösung ermöglicht die Generierung strukturierter System-Prompts (Instructions) für KI-Agenten, basierend auf Parametern wie Agenten-Name, Zweck, Tools und Einschränkungen.

## UI-Verwendung
Die Benutzeroberfläche stellt Eingabefelder für Name, Zweck, Tools und Constraints bereit. Nach dem Absenden wird ein strukturierter System-Prompt für den Agenten generiert, der direkt in die Zwischenablage kopiert werden kann.

## API / Schnittstelle
Diese Lösung bietet eine REST-API-Schnittstelle, die es erlaubt, Instruktionen programmatisch zu generieren.

### POST `/api/minimal-solutions/ai_agent_instruction_builder`

**Request-Beispiel (JSON):**
```json
{
  "agent_name": "Support Bot",
  "purpose": "Answer customer queries",
  "tools": "search_db, get_weather",
  "constraints": "Be polite, do not answer non-support questions"
}
```

**Response-Beispiel (JSON):**
```json
{
  "status": "success",
  "data": {
    "instruction": "You are Support Bot. Your primary purpose is to Answer customer queries.\n\nYou have access to the following tools:\n- search_db\n- get_weather\n\nYou must strictly adhere to the following constraints:\n- Be polite, do not answer non-support questions"
  }
}
```

## Externe Verwendung
Die Schnittstelle kann problemlos von externen Systemen, wie z.B. Automatisierungstools (n8n, Make), Chatbots oder Backend-Diensten angesprochen werden, um dynamisch System-Prompts zu generieren. Man muss lediglich einen HTTP POST-Request mit den entsprechenden Parametern im JSON-Format an den Endpunkt senden.
