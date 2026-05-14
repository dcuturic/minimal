# Landingpage Mapper

Der **Landingpage Mapper** ist eine Minimal-Lösung der CraftHoster Plattform. Diese Lösung ermöglicht es, Landingpage-Daten (wie Topic, Target und weitere Optionen) zu erfassen und eine Mapping-Struktur zurückzugeben.

## Externe API-Nutzung

Die Funktionalität des Landingpage Mappers steht auch als API-Schnittstelle zur Verfügung und kann von externen Diensten angesprochen werden.

### Endpunkt
`POST /api/minimal-solutions/landingpage_mapper`

### Request-Beispiel
Senden Sie einen POST-Request mit einem JSON-Body, der `topic`, `target` und optional `options` enthält.

```json
{
  "topic": "Produkt-Launch",
  "target": "Neukunden",
  "options": {
    "strategy": "direct",
    "include_metadata": true
  }
}
```

### Response-Beispiel
Die API antwortet im Standard-Format der Minimal-Lösungen Plattform:

```json
{
  "status": "success",
  "data": {
    "topic": "Produkt-Launch",
    "target": "Neukunden",
    "options": {
      "strategy": "direct",
      "include_metadata": true
    },
    "mapper_id": "map_123456",
    "timestamp": "2026-05-13T12:00:00Z",
    "mapped": true
  }
}
```
