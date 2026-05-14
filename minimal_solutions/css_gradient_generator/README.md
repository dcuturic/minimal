# CSS Gradient Generator

Ein Tool zum einfachen Generieren von linearen und radialen CSS-Farbverläufen (Gradients). 

## Schnittstelle

Die API erwartet einen POST-Request unter `/api/minimal-solutions/css_gradient_generator`.

### Request

```json
{
  "type": "linear",
  "colors": ["#FF5733", "#3333FF"],
  "angle": 90
}
```

### Response

```json
{
  "status": "success",
  "data": {
    "css": "linear-gradient(90deg, #FF5733, #3333FF)"
  }
}
```

Optionale Parameter:
- `angle`: Nur relevant für den Typ `linear` (Standard: 90).
- `type`: Entweder `"linear"` oder `"radial"` (Standard: "linear").
