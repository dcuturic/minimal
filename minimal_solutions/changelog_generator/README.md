# Changelog Generator

Eine Minimal-Lösung zum automatisierten Generieren von Markdown-formatierten Changelogs aus einer Liste von Änderungen, einer Version und einem optionalen Datum.

## Externe Nutzung (API)

Diese Minimal-Lösung bietet eine API-Schnittstelle, die von externen Systemen genutzt werden kann, um programmgesteuert Changelogs zu generieren.

### API-Endpunkt

`POST /api/minimal-solutions/changelog_generator`

### Request-Format (JSON)

Senden Sie einen POST-Request mit folgendem JSON-Body:

```json
{
  "version": "1.0.0",
  "date": "2026-05-12",
  "changes": [
    "Added new feature X",
    "Fixed bug Y",
    "Improved performance"
  ]
}
```

* `version` (String, erforderlich): Die Versionsnummer.
* `changes` (Array von Strings, erforderlich): Eine Liste von Änderungen.
* `date` (String, optional): Das Datum (z.B. "2026-05-12"). Wenn nicht angegeben, wird standardmäßig das heutige Datum verwendet.

### Response-Format (JSON)

Die API antwortet im Standard-Plattform-Format:

```json
{
  "status": "success",
  "data": {
    "result": "## [1.0.0] - 2026-05-12\n\n- Added new feature X\n- Fixed bug Y\n- Improved performance"
  }
}
```

Im Fehlerfall (z.B. fehlende Pflichtfelder) sieht die Antwort so aus:

```json
{
  "status": "error",
  "message": "Fehlende Felder: version, changes",
  "data": null
}
```

## Integration in die Plattform

- **Ordner:** `minimal_solutions/changelog_generator`
- **UI-Route:** `/minimal-solutions/changelog_generator`
- **API-Route:** `/api/minimal-solutions/changelog_generator`
