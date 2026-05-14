# Testimonial Card Generator

Der Testimonial Card Generator ist eine Minimal-Lösung zur einfachen Erstellung von professionellen Testimonial-Karten (Kundenstimmen). Er nimmt Name, Rolle und das Zitat als Input und generiert daraus direkt nutzbaren HTML- und CSS-Code für Webseiten.

## Externe Nutzung (API)

Die Lösung bietet eine API, um Testimonial-Karten automatisiert zu generieren.

**Endpunkt:** `POST /api/minimal-solutions/testimonial_card_generator`

**Request-Beispiel (JSON):**
```json
{
  "name": "Jane Doe",
  "role": "CEO at TechCorp",
  "quote": "This product changed our workflow completely!"
}
```

**Response-Beispiel (JSON):**
```json
{
  "status": "success",
  "data": {
    "name": "Jane Doe",
    "role": "CEO at TechCorp",
    "quote": "This product changed our workflow completely!",
    "html": "<div class=\"tc-result-card\"...",
    "css": ".tc-result-card { ... }"
  }
}
```

## Validierung
- `name` ist ein Pflichtfeld.
- `role` ist ein Pflichtfeld.
- `quote` ist ein Pflichtfeld.
