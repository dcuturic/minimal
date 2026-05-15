# Minecraft Masker

Minecraft Masker ist eine Minimal-Lösung, um Minecraft-Daten (wie Server-Logs, Chat-Verläufe, Spieler-IPs oder Passwörter) sicher zu maskieren und zu anonymisieren.
Diese Schnittstelle kann von externen Systemen angesprochen werden, um Maskierungsvorgänge automatisiert durchzuführen.

## Externe Verwendung

Die Schnittstelle kann von externen Systemen aufgerufen werden, indem ein `POST`-Request mit den entsprechenden Parametern (`input_text`, `options`, `mode`) als JSON-Body gesendet wird.

**API Endpoint:**
`POST /api/minimal-solutions/minecraft_masker`

### Request-Beispiel

```json
{
  "input_text": "Player123 logged in from 192.168.1.100",
  "options": [
    "mask_ips",
    "mask_usernames"
  ],
  "mode": "mask"
}
```

### Response-Beispiel

```json
{
  "success": true,
  "data": {
    "input_text": "Player123 logged in from 192.168.1.100",
    "mode": "mask",
    "options": [
      "mask_ips",
      "mask_usernames"
    ],
    "message": "Maskierung erfolgreich generiert."
  },
  "error": null,
  "warnings": [],
  "meta": {}
}
```
