# Landingpage Preview API

Die Landingpage Preview API generiert basierend auf den bereitgestellten Parametern eine HTML-Vorschau für eine Landingpage. Diese Lösung kann in externen Systemen integriert werden, um schnell ansprechende Landingpage-Strukturen zu visualisieren.

## Externe Verwendung

Um die Schnittstelle extern zu verwenden, sende einen HTTP POST-Request an den Endpunkt. Die Anfrage muss im JSON-Format vorliegen und die erforderlichen Felder `topic` und `target` enthalten. Optional kann ein `options`-Feld als String oder Objekt übergeben werden.

**Endpunkt:**
`POST /api/minimal-solutions/landingpage_preview`

### Request-Beispiel

```json
{
  "topic": "Modern AI SaaS",
  "target": "Developers and Tech Founders",
  "options": {
    "features": "Dark mode, easy integration",
    "tone": "professional",
    "primary_color": "#10b981"
  }
}
```

### Response-Beispiel

```json
{
  "status": "success",
  "data": {
    "preview_html": "<div style=\"font-family: system-ui, sans-serif; max-width: 800px; margin: 0 auto; padding: 48px; text-align: center; background: #ffffff; border-radius: 12px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06); border: 1px solid #e5e7eb;\">\n    <h1 style=\"color: #111827; font-size: 3rem; font-weight: 800; letter-spacing: -0.025em; margin-bottom: 24px; line-height: 1.2;\">Modern AI SaaS</h1>\n    <p style=\"color: #4b5563; font-size: 1.25rem; margin-bottom: 20px; line-height: 1.5; max-width: 600px; margin-left: auto; margin-right: auto;\">Designed specifically for: <strong style=\"color: #111827;\">Developers and Tech Founders</strong></p>\n    <p style='color: #6b7280; font-size: 1.125rem; margin-bottom: 20px;'>Features: Dark mode, easy integration</p>\n    <button style=\"background-color: #10b981; color: white; padding: 16px 32px; border-radius: 8px; font-weight: 600; font-size: 1.125rem; border: none; cursor: pointer; transition: opacity 0.2s;\">\n        Get Started Now\n    </button>\n    <div style=\"margin-top: 48px; padding-top: 24px; border-top: 1px solid #e5e7eb; color: #9ca3af; font-size: 0.875rem;\">\n        Tone: professional | Auto-generated Preview\n    </div>\n</div>",
    "meta": {
      "topic": "Modern AI SaaS",
      "target": "Developers and Tech Founders",
      "options": {
        "features": "Dark mode, easy integration",
        "tone": "professional",
        "primary_color": "#10b981"
      }
    }
  }
}
```
