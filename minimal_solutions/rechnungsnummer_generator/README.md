# Rechnungsnummer Generator

Ein Minimal-Lösung API-Service zur Generierung von fortlaufenden Rechnungsnummern nach einem definierten Muster.

## Beschreibung
Der Rechnungsnummer Generator erstellt eine Liste von Rechnungsnummern, basierend auf optionalen Parametern wie Präfix und Jahr, einer Startnummer und der gewünschten Anzahl an zu generierenden Nummern.

Die generierten Nummern folgen dem Format: `[Präfix]-[Jahr]-[Laufende Nummer]`. Wenn Präfix oder Jahr weggelassen werden, wird das Format entsprechend angepasst. Die laufende Nummer wird immer mit führenden Nullen aufgefüllt (z.B. `0001`).

## Externe Verwendung

Die Schnittstelle kann extern über HTTP POST Anfragen an den Endpunkt `/api/minimal-solutions/rechnungsnummer_generator` genutzt werden.
Alle Anfragen müssen im JSON-Format gesendet werden (`Content-Type: application/json`).

### Parameter

| Feld | Typ | Erforderlich | Beschreibung |
|------|-----|--------------|--------------|
| `start_number` | Integer | Ja | Die Nummer, bei der die Zählung beginnen soll (min: 1). |
| `count` | Integer | Ja | Die Anzahl der zu generierenden Rechnungsnummern (min: 1, max: 1000). |
| `prefix` | String | Nein | Ein optionales Präfix für die Rechnungsnummer (z.B. "RE"). |
| `year` | String/Integer | Nein | Ein optionales Jahr für die Rechnungsnummer (z.B. "2026"). |

### Request-Beispiel

```bash
curl -X POST https://your-domain.com/api/minimal-solutions/rechnungsnummer_generator \
  -H "Content-Type: application/json" \
  -d '{
    "prefix": "RE",
    "year": "2026",
    "start_number": 1,
    "count": 3
  }'
```

### Response-Beispiel

```json
{
  "status": "success",
  "data": {
    "numbers": [
      "RE-2026-0001",
      "RE-2026-0002",
      "RE-2026-0003"
    ],
    "count": 3,
    "pattern": "RE-2026-0000"
  }
}
```
