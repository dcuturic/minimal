# Landingpage Checker - Minimal Solution

Dieses Verzeichnis enthält die Minimal-Lösung "Landingpage Checker".

## Externe Nutzung (API)

Die Lösung bietet eine externe Schnittstelle (API), um Landingpage-Checks durchzuführen.

**Endpoint:**
`POST /api/minimal-solutions/landingpage_checker`

**Request-Beispiel (JSON):**
```json
{
  "topic": "Modern AI SaaS",
  "target": "Developers and Tech Founders",
  "options": "Check spelling, check CTA"
}
```

**Response-Beispiel (JSON):**
```json
{
  "status": "success",
  "data": {
    "check_result": "Dies ist ein generierter Check für die Landingpage zum Thema 'Modern AI SaaS'.\n\nZielgruppe: Developers and Tech Founders\nOptionen: Check spelling, check CTA\n\nDie Struktur der Landingpage sieht gut aus. Die Überschriften sind klar formuliert. Empfehlung: Mehr Call-to-Action Buttons einfügen, um die Conversion zu steigern.",
    "meta": {
      "topic": "Modern AI SaaS",
      "target": "Developers and Tech Founders",
      "options": "Check spelling, check CTA"
    }
  }
}
```

## UI-Komponente
Die UI ist in `landingpage_checker_component.html` definiert und kann über die Route `/minimal-solutions/landingpage_checker` aufgerufen werden. Dort findet sich auch eine interaktive API-Doku-Box.
