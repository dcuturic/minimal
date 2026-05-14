# Farbkonverter Minimal-Lösung

Die Farbkonverter-Schnittstelle ermöglicht die automatische Umrechnung von Farbwerten zwischen verschiedenen Formaten (HEX, RGB, RGBA, HSL). Die API kann extern genutzt werden, um eingegebene Farbwerte zu validieren und in alle Standard-Web-Formate zu konvertieren.

## Endpunkt

`POST /api/minimal-solutions/farbkonverter`

## Verwendung

Senden Sie einen POST-Request an den Endpunkt mit einem JSON-Body, der den Parameter `color_value` enthält. Dieser kann als HEX (z.B. `#FF5733`), RGB (z.B. `rgb(255, 87, 51)`), RGBA oder HSL übergeben werden.

### Request-Beispiel

```json
{
  "color_value": "#FF5733"
}
```

### Response-Beispiel

```json
{
  "status": "success",
  "data": {
    "hex": "#FF5733",
    "rgb": "rgb(255, 87, 51)",
    "rgba": "rgba(255, 87, 51, 1)",
    "hsl": "hsl(11, 100%, 60%)"
  }
}
```
