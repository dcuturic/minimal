# Hashtag Generator

Dies ist eine Minimal-Lösung für die Generierung von relevanten Hashtags basierend auf einem Thema und einer Zielgruppe. 
Sie bietet sowohl eine visuelle Oberfläche als auch eine API-Schnittstelle.

## API-Nutzung

Die Schnittstelle kann extern verwendet werden, indem ein POST-Request an den entsprechenden Endpunkt gesendet wird.
Dabei muss als Body ein JSON-Objekt mit dem Thema (`topic`), der Zielgruppe (`audience`) und der gewünschten Anzahl an Hashtags (`count`) übergeben werden.

**Endpunkt:**
`POST /api/minimal-solutions/hashtag_generator`

### Request-Beispiel

```json
{
  "topic": "Artificial Intelligence",
  "audience": "general",
  "count": 5
}
```

### Response-Beispiel

```json
{
  "status": "success",
  "data": {
    "hashtags": "#ArtificialIntelligence #ArtificialIntelligenceLife #ArtificialIntelligenceTips #ArtificialIntelligenceCommunity #ArtificialIntelligenceVibes",
    "list": [
      "#ArtificialIntelligence",
      "#ArtificialIntelligenceLife",
      "#ArtificialIntelligenceTips",
      "#ArtificialIntelligenceCommunity",
      "#ArtificialIntelligenceVibes"
    ]
  }
}
```
