# SEO Cleaner

Dies ist die Minimal-Lösung für den SEO Cleaner.

## Struktur

- `demo.html`: Benutzeroberfläche und API-Dokumentation
- `api.py` / `seo_cleaner_api.py`: API-Endpunkte
- `validation.py` / `seo_cleaner_validation.py`: Validierungslogik
- `demo.json`: Beispieldaten

## Externe Nutzung der API

Die SEO Cleaner Schnittstelle kann extern über HTTP-POST-Requests angesprochen werden.

**Endpunkt:**
`POST /api/minimal-solutions/seo_cleaner`

**Nutzung:**
Sende einen JSON-Body mit den Parametern `topic` (String), `target` (String) und optionalen `options` (Object) an den Endpunkt.

**Beispiel Request (cURL):**
```bash
curl -X POST "http://localhost:5000/api/minimal-solutions/seo_cleaner" \
     -H "Content-Type: application/json" \
     -d '{
           "topic": "Content Marketing",
           "target": "Beginners",
           "options": {"remove_duplicates": true}
         }'
```

**Erwartete Response:**
```json
{
  "status": "success",
  "data": {
    "topic": "Content Marketing",
    "target": "Beginners",
    "options": {
      "remove_duplicates": true
    },
    "clean_status": "success",
    "clean_items": 5,
    "message": "Daten für 'Content Marketing' erfolgreich bereinigt."
  }
}
```
