# SVG Icon Generator

Der SVG Icon Generator ist eine Minimal-Lösung, mit der schnell und einfach Vektor-Icons (SVG) in verschiedenen Formen, Farben und mit einem optionalen Text-Label (z.B. Buchstaben) generiert werden können. Die Lösung bietet eine interaktive UI sowie eine API zur programmatischen Nutzung.

## Features

- **Icon Formen:** Kreis, Quadrat, abgerundetes Quadrat, Stern, Sechseck, Dreieck, Raute, Schild.
- **Farbanpassung:** Die Hauptfarbe des Icons kann per HEX-Code frei gewählt werden.
- **Text-Label:** Optionaler Text im Zentrum des Icons (maximal 2 Zeichen, z.B. "A", "JS", "1").
- **Export:** Das generierte Icon kann direkt in die Zwischenablage kopiert oder als `.svg`-Datei heruntergeladen werden.

## API-Nutzung (Schnittstelle)

Die Funktionalität kann auch als API in eigenen Projekten verwendet werden.

### Endpoint

**POST** `/api/minimal-solutions/svg_icon_generator`

### Request (JSON)

```json
{
  "shape": "circle",
  "color": "#3b82f6",
  "label": "A"
}
```

### Response (JSON)

```json
{
  "status": "success",
  "data": {
    "svg_code": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 100 100\" width=\"100%\" height=\"100%\"><circle cx=\"50\" cy=\"50\" r=\"50\" fill=\"#3b82f6\" /><text x=\"50\" y=\"50\" font-family=\"Arial, sans-serif\" font-size=\"40\" fill=\"#ffffff\" text-anchor=\"middle\" dominant-baseline=\"central\" font-weight=\"bold\">A</text></svg>",
    "shape": "circle",
    "color": "#3b82f6",
    "label": "A"
  }
}
```

## Validierung
- `shape`: Muss einer der erlaubten Werte sein (`circle`, `square`, `rounded`, `star`, `hexagon`, `triangle`, `diamond`, `shield`).
- `color`: Muss ein gültiger HEX-Farbcode sein (z.B. `#ff0000` oder `#f00`).
- `label`: Optional, maximal 2 Zeichen lang.
