# Landingpage Section Generator

Der **Landingpage Section Generator** ist eine Minimal-Lösung, die es erlaubt, verschiedene Landingpage-Sektionen (wie Hero, Features, Testimonials, CTA, FAQ) dynamisch anhand eines Themas zu generieren.

## Externe Nutzung (API / Schnittstelle)

Diese Lösung kann nicht nur über die Benutzeroberfläche, sondern auch extern als API genutzt werden. So kannst du Landingpage-Strukturen direkt in deine eigenen Anwendungen integrieren.

### Endpunkt

`POST /api/minimal-solutions/landingpage_section_generator`

### Parameter (JSON Body)

- `section_type` (String): Der Typ der Sektion (z. B. `hero`, `features`, `testimonials`, `cta`, `faq`).
- `topic` (String): Das Thema oder der Produktname (z. B. `AI Content Generator`).

### Request-Beispiel

```json
{
  "section_type": "hero",
  "topic": "AI Content Generator"
}
```

### Response-Beispiel

```json
{
  "status": "success",
  "data": {
    "result": {
      "type": "hero",
      "headline": "Supercharge your AI Content Generator",
      "subheadline": "The best way to manage your AI Content Generator workflow efficiently and effortlessly.",
      "call_to_action": "Get Started Now"
    }
  }
}
```
