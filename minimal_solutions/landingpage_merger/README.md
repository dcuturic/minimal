# Landingpage Merger

## Beschreibung
Der **Landingpage Merger** ist eine Minimal-Lösung, mit der sich verschiedene Landingpage-Eingaben (z.B. Topic, Target und weitere Optionen) zu einer Einheit zusammenführen lassen. Dies dient beispielsweise dazu, generische Textblöcke und Spezifikationen in ein einheitliches Format zu überführen.

## API-Schnittstelle (Externe Nutzung)

Dieser Service kann extern als API genutzt werden, um Landingpage-Daten programmgesteuert zusammenzuführen.

**Endpunkt:**
`POST /api/minimal-solutions/landingpage_merger`

**Header:**
`Content-Type: application/json`

**Request-Beispiel:**
```json
{
  "topic": "Produkt-Launch",
  "target": "Neukunden",
  "options": {
    "strategy": "combine"
  }
}
```

**Response-Beispiel:**
```json
{
  "status": "success",
  "data": {
    "topic": "Produkt-Launch",
    "target": "Neukunden",
    "options": {
      "strategy": "combine"
    },
    "merger_id": "mrg_123456",
    "timestamp": "2026-05-13T12:00:00Z",
    "merged": true
  }
}
```
