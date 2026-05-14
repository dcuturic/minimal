# Hosting Formatter

## Beschreibung
Die Minimal-Lösung "Hosting Formatter" bietet eine einfache Schnittstelle, um Hosting-Daten (wie Host, IP-Adresse etc.) strukturiert zu formatieren und darzustellen. Die Lösung besteht aus einer grafischen Benutzeroberfläche (`demo.html`) und einer API.

## Externe Verwendung
Die Schnittstelle kann problemlos von externen Anwendungen konsumiert werden. Sende dazu einfach einen `POST`-Request im JSON-Format an den entsprechenden API-Endpunkt.

**Endpunkt:**
`POST /api/minimal-solutions/hosting_formatter`

### Request-Beispiel

```json
{
  "source": "{\"host\": \"example.com\", \"ip\": \"192.168.1.1\"}",
  "config": "{}",
  "mode": "standard"
}
```

### Response-Beispiel

Bei erfolgreicher Formatierung liefert die API folgendes JSON zurück:

```json
{
  "result": "Host: example.com\nIP: 192.168.1.1",
  "status": "success"
}
```
