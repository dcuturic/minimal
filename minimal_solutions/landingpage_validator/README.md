# Landingpage Validator

Die Minimal-Lösung "Landingpage Validator" erlaubt es, geplante Landingpage-Daten (Topic, Target Audience, Options) zu validieren und Feedback zur Qualität der Eingaben zu erhalten.

## Externe Verwendung (API)

Die Schnittstelle ist über `POST /api/minimal-solutions/landingpage_validator` erreichbar.

### Request-Beispiel
```json
{
  "topic": "Modern AI SaaS",
  "target": "Developers and Tech Founders",
  "options": "Dark mode, easy integration, low latency"
}
```

### Response-Beispiel
```json
{
  "status": "success",
  "data": {
    "result": "Validation Report:\n------------------\n✅ Topic length is optimal.\n✅ Target audience is specific.\n✅ Additional options recognized."
  }
}
```

## Benutzeroberfläche (UI)

Die visuelle Oberfläche ist unter `/minimal-solutions/landingpage_validator` erreichbar.
