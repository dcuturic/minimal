# Minecraft MOTD Preview

Eine Minimal-Lösung, um Minecraft MOTD (Message of the Day) Texte mit Farb- und Formatierungscodes (wie `&a`, `&l`) zu parsen und als HTML-Vorschau darzustellen.

## Externe API-Nutzung

Die Minimal-Lösung bietet eine REST-API-Schnittstelle, die von externen Anwendungen genutzt werden kann.

**Endpoint:**
`POST /api/minimal-solutions/minecraft_motd_preview`

**Request-Body:**
```json
{
  "motd_text": "&aWelcome to our\n&cAwesome Server"
}
```

**Erfolgreiche Response:**
```json
{
  "status": "success",
  "data": {
    "motd_text": "&aWelcome to our\n&cAwesome Server"
  }
}
```

## UI Demo

Die Benutzeroberfläche ermöglicht es, den MOTD Text einzugeben, eine sofortige Vorschau im Minecraft-Look zu generieren und das gerenderte HTML in die Zwischenablage zu kopieren.
