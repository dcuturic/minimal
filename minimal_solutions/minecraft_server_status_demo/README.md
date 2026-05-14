# Minecraft Server Status Demo

Diese Minimal-Lösung bietet eine einfache Oberfläche und eine API, um den Status eines Minecraft-Servers (Online-Status, Spieleranzahl, Version etc.) abzufragen.

## Externe Nutzung (API)

Die Schnittstelle kann problemlos von externen Anwendungen konsumiert werden. Sende dazu einen `POST` Request an den Endpunkt mit dem Host und optional dem Port des Minecraft-Servers.

**Endpunkt:**
`POST /api/minimal-solutions/minecraft_server_status_demo`

**Request-Beispiel (JSON):**
```json
{
  "host": "mc.hypixel.net",
  "port": 25565
}
```

**Response-Beispiel (JSON):**
```json
{
  "status": "success",
  "data": {
    "host": "mc.hypixel.net",
    "port": 25565,
    "online": true,
    "players_online": 35000,
    "players_max": 100000,
    "version": "1.20.1",
    "motd": "A Minecraft Server"
  }
}
```

Die API gibt in jedem Fall ein standardisiertes JSON-Objekt zurück. Bei Fehlern (z.B. ungültiger Host oder Server nicht erreichbar) ändert sich der `status` auf `error` und eine entsprechende `message` wird zurückgegeben.
