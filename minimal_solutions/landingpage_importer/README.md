# Landingpage Importer

Der Landingpage Importer ist eine Minimal-Lösung, mit der strukturierte Landingpage-Daten (wie Topic, Target Audience und weitere Optionen) über eine API oder die integrierte UI importiert und validiert werden können.

## API Nutzung (Schnittstelle)

Die Schnittstelle kann extern über REST verwendet werden, um automatisiert Landingpage-Importe durchzuführen.

### Endpunkt
`POST /api/minimal-solutions/landingpage_importer`

### Request Header
- `Content-Type: application/json`

### Request Body
Es wird ein JSON-Objekt mit folgenden Feldern erwartet:
- `topic` (string, erforderlich): Das Hauptthema der Landingpage.
- `target` (string, erforderlich): Die Zielgruppe der Landingpage.
- `options` (string, optional): Zusätzliche Optionen oder ein Link zu den zu importierenden Daten.

**Beispiel-Request:**
```json
{
  "topic": "Modern AI SaaS",
  "target": "Developers and Tech Founders",
  "options": "Include meta tags, import images"
}
```

### Response
Die API antwortet im Standard-Format der CraftHoster Minimal Solutions Platform.

**Beispiel-Response:**
```json
{
  "status": "success",
  "data": {
    "imported_data": "Landingpage Data Imported:\n\nTopic: Modern AI SaaS\nTarget Audience: Developers and Tech Founders\nOptions: Include meta tags, import images",
    "meta": {
      "topic": "Modern AI SaaS",
      "target": "Developers and Tech Founders",
      "options": "Include meta tags, import images"
    }
  }
}
```

## Fehlerbehandlung
Falls Felder fehlen oder ungültig sind, gibt die API einen strukturierten Fehler zurück:

```json
{
  "status": "error",
  "message": "Validation failed",
  "details": "Topic and Target Audience are required."
}
```
