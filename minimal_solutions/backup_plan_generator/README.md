# Backup Plan Generator

Ein Minimal-Lösungs-Tool, um strukturierte Backup-Pläne auf Basis von Frequenz, Aufbewahrungsdauer und Speicherart zu generieren.

## UI-Funktionalitäten

Die Benutzeroberfläche bietet:
- Dropdown zur Auswahl der Backup-Frequenz (Hourly, Daily, Weekly, Monthly)
- Eingabefeld für die Aufbewahrungsdauer in Tagen
- Dropdown für die Speicherart (Local, AWS S3, Azure Blob, Google Cloud Storage)
- Eine Vorschau des generierten Backup-Plans als JSON
- Einen Button zum schnellen Kopieren des Ergebnisses

## API-Nutzung

Diese Minimal-Lösung bietet eine REST-API-Schnittstelle, die extern angebunden werden kann.

**Endpunkt:** `POST /api/minimal-solutions/backup_plan_generator`

### Request-Beispiel

```json
{
  "frequency": "daily",
  "retention_days": 30,
  "storage_type": "s3"
}
```

### Response-Beispiel

```json
{
  "status": "success",
  "data": {
    "plan_id": "bp_20260512_daily_30_s3",
    "frequency": "daily",
    "retention_days": 30,
    "storage_type": "s3",
    "schedule_cron": "0 0 * * *",
    "retention_policy": "Delete backups older than 30 days",
    "storage_details": {
      "type": "AWS S3",
      "recommended_class": "Standard",
      "encryption": "AES-256"
    },
    "estimated_monthly_cost_per_gb": "$0.023",
    "required_actions": [
      "Create S3 bucket with versioning enabled",
      "Configure lifecycle rule to expire current versions after 30 days",
      "Set up IAM role for backup script with putObject permissions",
      "Schedule daily execution at midnight"
    ]
  }
}
```

## Fehlerbehandlung

Die API gibt klare Fehlermeldungen bei ungültigen Eingaben zurück, z.B. wenn die `retention_days` fehlt oder kleiner-gleich 0 ist. Das Fehlerformat entspricht dem Standard der Plattform:

```json
{
  "status": "error",
  "message": "Ungültige Aufbewahrungsdauer"
}
```
