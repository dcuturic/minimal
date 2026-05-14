# Uptime Badge Generator

Ein Minimal-Lösungstool, das SVG-Badges für Uptime-Monitoring-Services generiert. Diese Badges können in READMEs, Statusseiten oder anderen Dokumentationen eingebunden werden, um den aktuellen Status und die prozentuale Erreichbarkeit darzustellen.

## Externe API-Schnittstelle

Die Schnittstelle dieses Tools kann problemlos von externen Anwendungen, Monitoring-Skripten oder CI/CD-Pipelines angesprochen werden.

### Endpunkt

`POST /api/minimal-solutions/uptime_badge_generator`

### Request

Der Request muss als JSON formatiert sein und einen `status` (up, down, maintenance) sowie die `uptime_percent` enthalten:

```json
{
  "status": "up",
  "uptime_percent": 99.99
}
```

### Response

Bei einem erfolgreichen Aufruf wird die generierte SVG-Grafik sowie ein vorbereiteter Markdown-Code als JSON zurückgegeben:

```json
{
  "status": "success",
  "data": {
    "svg": "<svg>...</svg>",
    "markdown": "![Uptime Badge](data:image/svg+xml;base64,...)"
  }
}
```

## Integration in externe Systeme

Um die Badges in Ihre Anwendungen einzubinden, können Sie das bereitgestellte Markdown (`data.markdown`) direkt in eine Markdown-Datei übernehmen, oder das SVG (`data.svg`) für den direkten HTML-Einsatz verwenden.
