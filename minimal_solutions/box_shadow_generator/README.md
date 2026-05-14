# Box Shadow Generator
Ein Tool zur visuellen Erstellung von CSS Box-Shadow Effekten.

## Externe Nutzung (API / Schnittstelle)
Die Funktionalität des Box Shadow Generators kann auch als externe API genutzt werden, um dynamisch CSS-Code für Schatten-Effekte auf Basis von Parametern zu generieren.

### Request
Sende einen `POST` Request an den Endpunkt `/api/minimal-solutions/box_shadow_generator`.

**Body-Parameter:**
- `x` (int): X-Offset in Pixeln.
- `y` (int): Y-Offset in Pixeln.
- `blur` (int): Blur-Radius in Pixeln.
- `spread` (int): Spread-Radius in Pixeln.
- `opacity` (float): Deckkraft der Farbe (0.0 bis 1.0).
- `color` (string): HEX-Farbcode für den Schatten.
- `inset` (boolean): `true` für Inset-Schatten, `false` für Drop-Shadow.

**Beispiel:**
```json
{
  "x": 10,
  "y": 10,
  "blur": 20,
  "spread": 0,
  "opacity": 0.5,
  "color": "#000000",
  "inset": false
}
```

### Response
Die API antwortet im Standardformat und liefert den fertigen CSS-Code zurück.

**Beispiel:**
```json
{
  "status": "success",
  "data": {
    "css": "box-shadow: 10px 10px 20px 0px rgba(0, 0, 0, 0.5);"
  }
}
```
