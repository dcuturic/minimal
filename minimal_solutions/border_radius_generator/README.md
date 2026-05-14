# Border Radius Generator

Eine Minimal-Lösung, um visuell und per API CSS Border-Radius-Werte zu generieren.

## UI-Verwendung
Die UI ermöglicht das Einstellen von vier verschiedenen Eckradien (Top Left, Top Right, Bottom Right, Bottom Left) über Slider. Das Ergebnis wird sofort als visuelle Box-Vorschau und als kopierbarer CSS-Code (`border-radius: ...;`) angezeigt.

## API / Schnittstelle

Dieser Service kann extern als API genutzt werden, um dynamisch CSS-Code für Border-Radius-Effekte auf Basis von Parametern zu generieren.

**Endpunkt:** `POST /api/minimal-solutions/border_radius_generator`

### Request-Beispiel

```json
{
  "top_left": 10,
  "top_right": 20,
  "bottom_right": 30,
  "bottom_left": 40
}
```

### Response-Beispiel

```json
{
  "status": "success",
  "data": {
    "css": "border-radius: 10px 20px 30px 40px;"
  }
}
```

## Integration
- UI-Route: `/minimal-solutions/border_radius_generator`
- API-Route: `/api/minimal-solutions/border_radius_generator`
- Ordner: `minimal_solutions/border_radius_generator`
