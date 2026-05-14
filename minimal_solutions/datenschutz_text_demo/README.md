# Datenschutz Text Demo

Diese Minimal-Lösung bietet ein einfaches Formular sowie eine REST-API, um einen standardisierten (und vereinfachten) Datenschutz-Text zu generieren. Nutzer können verschiedene Optionen (Cookies, Analytics, Kontaktformular) sowie ihren Hosting-Provider angeben. 

Die generierten Texte dienen lediglich als Beispiele und stellen keine Rechtsberatung dar.

## Externe Nutzung (API)

Die Lösung bietet eine REST-API-Schnittstelle, die von externen Applikationen genutzt werden kann, um programmgesteuert Datenschutz-Texte zu generieren.

### Endpunkt

`POST /api/minimal-solutions/datenschutz_text_demo`

### Request-Beispiel (JSON)

```json
{
  "uses_cookies": true,
  "uses_analytics": true,
  "uses_contact_form": false,
  "hosting_provider": "Hetzner Online GmbH"
}
```

### Response-Beispiel (JSON)

```json
{
  "status": "success",
  "data": {
    "text": "1. Datenschutz auf einen Blick\n\nAllgemeine Hinweise\nDie folgenden Hinweise geben einen einfachen Überblick darüber, was mit Ihren personenbezogenen Daten passiert, wenn Sie diese Website besuchen.\n\n2. Hosting\nWir hosten die Inhalte unserer Website bei folgendem Anbieter:\nHetzner Online GmbH\n\n3. Cookies\nUnsere Website verwendet sogenannte „Cookies“. Das sind kleine Textdateien, die auf Ihrem Endgerät abgelegt werden.\n\n4. Analyse-Tools und Werbung\nDiese Website nutzt Funktionen eines Webanalysedienstes.\n\n"
  }
}
```
