# Random Name Generator

Eine Minimal-Lösung zum Generieren von zufälligen Namen aus verschiedenen Kategorien. Die Anwendung bietet eine interaktive Oberfläche und eine REST-API.

## API / Schnittstelle

Dieser Service kann extern als API genutzt werden, um programmgesteuert zufällige Namen abzurufen.

### Endpunkt
`POST /api/minimal-solutions/random_name_generator`

### Request-Beispiel
```json
{
  "category": "project",
  "count": 3
}
```
* `category` kann z.B. project, server, bot, fantasy, scifi, nature sein.
* `count` ist eine Zahl zwischen 1 und 100.

### Response-Beispiel
```json
{
  "status": "success",
  "data": {
    "names": [
      "NexusCore",
      "QuantumSync",
      "AeroShift"
    ]
  }
}
```

## Integration in die Plattform
- **Ordner:** `minimal_solutions/random_name_generator`
- **UI Route:** `/minimal-solutions/random_name_generator`
- **API Endpoint:** `/api/minimal-solutions/random_name_generator`
