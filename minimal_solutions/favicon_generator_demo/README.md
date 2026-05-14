# Favicon Generator Demo

Die **Favicon Generator Demo** API kann in externen Applikationen verwendet werden, um dynamisch Favicons (als SVG) zu generieren. Durch Senden eines `POST`-Requests mit Buchstaben, Primärfarbe und der gewünschten Form wird das fertige SVG im JSON-Format zurückgegeben. Dies ist besonders nützlich für automatisierte Skripte, Plattformen oder CMS-Systeme, die personalisierte Platzhalter-Icons benötigen.

### API-Endpunkt

**POST** `/api/minimal-solutions/favicon_generator_demo`

### Request-Beispiel

```json
{
  "letters": "CH",
  "primary_color": "#3b82f6",
  "shape": "rounded"
}
```

### Response-Beispiel

```json
{
  "status": "success",
  "data": {
    "favicon_svg": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 512 512\">...</svg>"
  }
}
```
