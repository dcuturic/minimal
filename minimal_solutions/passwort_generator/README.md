# Passwort Generator

Eine Minimal-Lösung zur Generierung von sicheren, zufälligen Passwörtern. Die Anwendung bietet sowohl eine visuelle Oberfläche als auch eine REST-API.

## API / Schnittstelle

Dieser Service kann extern als API genutzt werden, um programmgesteuert Passwörter zu generieren. Die API empfängt Anfragen mit den gewünschten Konfigurationen (Länge, Zeichenarten) und liefert ein zufällig generiertes Passwort zurück.

### Endpunkt
`POST /api/minimal-solutions/passwort_generator`

### Request-Beispiel
```json
{
  "length": 16,
  "use_uppercase": true,
  "use_numbers": true,
  "use_symbols": true
}
```

### Response-Beispiel
```json
{
  "status": "success",
  "data": {
    "password": "aB3$eX9@lP2#kR7!",
    "length": 16,
    "strength": "strong"
  }
}
```

## Integration in die Plattform
- **Ordner:** `minimal_solutions/passwort_generator`
- **UI Route:** `/minimal-solutions/passwort_generator`
- **API Endpoint:** `/api/minimal-solutions/passwort_generator`
