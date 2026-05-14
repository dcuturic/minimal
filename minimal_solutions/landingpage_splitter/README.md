# Landingpage Splitter

Minimal solution for Landingpage Splitter.

Diese Minimal-Lösung bietet eine einfache Schnittstelle (API), um Landingpage-Daten in Segmente aufzuteilen oder zu strukturieren. Sie kann extern per HTTP POST-Request angesprochen werden.

## API Endpoint
`POST /api/minimal-solutions/landingpage_splitter`

### Request-Beispiel

Senden Sie einen HTTP POST-Request mit einem JSON-Body, der `topic` und `target` enthält:

```json
{
  "topic": "Produkt-Launch",
  "target": "Neukunden",
  "options": "{\"sections\": [\"header\", \"features\"]}"
}
```

### Response-Beispiel

Die API antwortet im Standard-Format der CraftHoster Plattform:

```json
{
  "status": "success",
  "data": {
    "topic": "Produkt-Launch",
    "target": "Neukunden",
    "options": "{\"sections\": [\"header\", \"features\"]}",
    "splitter_id": "spl_123456",
    "timestamp": "2026-05-13T12:00:00Z",
    "splitted": true
  }
}
```
