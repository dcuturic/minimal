# URL Encoder Decoder

Minimal-Lösung für das Encoding und Decoding von URLs.

## Externe Nutzung der API / Schnittstelle

Dieser Service kann extern als API genutzt werden, um programmgesteuert Texte für URLs zu enkodieren (URL-Encoding) und wieder zu dekodieren (URL-Decoding).

### Endpunkt
`POST /api/minimal-solutions/url_encoder_decoder`

### Request-Beispiel
```json
{
  "mode": "encode",
  "text": "Hello World!"
}
```
Hinweis: `mode` kann "encode" oder "decode" sein.

### Response-Beispiel (Success)
```json
{
  "status": "success",
  "data": {
    "result": "Hello%20World%21"
  }
}
```
