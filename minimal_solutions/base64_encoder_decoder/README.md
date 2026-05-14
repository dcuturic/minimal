# Base64 Encoder Decoder

Minimal-Lösung zum Kodieren und Dekodieren von Texten ins Base64-Format und zurück.

## Externe Verwendung (API)

Diese Minimal-Lösung bietet eine API, die extern genutzt werden kann, um programmgesteuert Texte in Base64 zu konvertieren oder aus Base64 zu entschlüsseln.

**Endpunkt**
`POST /api/minimal-solutions/base64_encoder_decoder`

### Request-Beispiel

Senden Sie einen POST-Request mit einem JSON-Body, der den `mode` (`encode` oder `decode`) und den Eingabetext (`text`) enthält:

```json
{
  "mode": "encode",
  "text": "Hello World"
}
```

### Response-Beispiel

Die API gibt bei Erfolg den kodierten oder dekodierten Text im `data.result` Feld zurück:

```json
{
  "status": "success",
  "data": {
    "result": "SGVsbG8gV29ybGQ="
  }
}
```
