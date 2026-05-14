# Log Highlighter API

Der Log Highlighter ist eine Minimal-Lösung, um rohen Log-Text zu analysieren und basierend auf den erkannten Log-Leveln (INFO, ERROR, WARN, DEBUG usw.) als formatiertes HTML mit entsprechenden CSS-Klassen zurückzugeben.

## API-Endpunkt

**URL:** `/api/minimal-solutions/log_highlighter`
**Methode:** `POST`
**Content-Type:** `application/json`

### Request-Beispiel

```json
{
  "log_text": "2023-10-27 10:00:00 INFO  Starting application\n2023-10-27 10:00:01 ERROR Connection failed"
}
```

### Response-Beispiel

```json
{
  "status": "success",
  "data": {
    "html": "<span class=\"log-line log-level-info\">2023-10-27 10:00:00 INFO  Starting application\n</span><span class=\"log-line log-level-error\">2023-10-27 10:00:01 ERROR Connection failed\n</span>",
    "lines": [
      {
        "text": "2023-10-27 10:00:00 INFO  Starting application\n",
        "level": "INFO"
      },
      {
        "text": "2023-10-27 10:00:01 ERROR Connection failed\n",
        "level": "ERROR"
      }
    ]
  }
}
```

## Verwendung

Die generierte `html`-Ausgabe kann direkt in ein DOM-Element eingefügt werden, um formatiertes und farblich hervorgehobenes Log-Protokoll darzustellen. Die dazugehörigen CSS-Klassen (z.B. `.log-level-info`, `.log-level-error`) sollten im Frontend entsprechend definiert sein.
