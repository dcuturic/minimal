# Risk Matrix Generator

Die Minimal-Lösung 'Risk Matrix Generator' bietet eine einfache Möglichkeit, Risiken basierend auf ihrer Wahrscheinlichkeit und ihren Auswirkungen zu bewerten und eine strukturierte Risikomatrix zu generieren. Die Schnittstelle kann per Web-Interface oder API genutzt werden.

## API-Nutzung

Die Funktionalität kann direkt über die API angesprochen werden. Hierfür muss ein POST-Request mit den Risikodaten im JSON-Format gesendet werden.

### Endpoint

`POST /api/minimal-solutions/risk_matrix_generator`

### Request-Beispiel

```json
{
  "risks": [
    {"name": "Server Crash", "probability": "High", "impact": "High"}
  ]
}
```

### Response-Beispiel

```json
{
  "status": "success",
  "data": {
    "matrix": "Risk Matrix\n========================================\n\n[HIGH RISK]\n- Server Crash (Prob: High, Impact: High)\n"
  }
}
```
