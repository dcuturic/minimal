# Landingpage Normalizer

Der **Landingpage Normalizer** ist eine Minimal-Lösung zur Normalisierung von Landingpage-Daten.

## Externe API-Nutzung

Die Schnittstelle kann von externen Diensten genutzt werden, um strukturierte oder unstrukturierte Landingpage-Eingaben (z. B. Topic, Target und Options) entgegenzunehmen, diese zu bereinigen und in ein standardisiertes Format (normalisiert) umzuwandeln. Dadurch wird sichergestellt, dass nachgelagerte Systeme konsistente Daten für Marketing-Kampagnen, Automatisierungen oder Analysen erhalten.

### API Endpunkt
`POST /api/minimal-solutions/landingpage_normalizer`

### Request-Beispiel
```json
{
  "topic": "Produkt-Launch",
  "target": "Neukunden",
  "options": {
    "case": "lower",
    "remove_special_chars": true
  }
}
```

### Response-Beispiel
```json
{
  "status": "success",
  "data": {
    "topic": "Produkt-Launch",
    "target": "Neukunden",
    "options": {
      "case": "lower",
      "remove_special_chars": true
    },
    "normalized_id": "norm_123456",
    "timestamp": "2026-05-13T12:00:00Z",
    "normalized": true
  }
}
```
