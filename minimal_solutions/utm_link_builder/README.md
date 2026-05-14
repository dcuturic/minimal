# UTM Link Builder

Die "UTM Link Builder" Minimal-Lösung ermöglicht die strukturierte Erstellung von URLs mit UTM-Tracking-Parametern (Urchin Tracking Module) für Marketing-Kampagnen.

## Funktionsweise

Benutzer können eine Basis-URL sowie die relevanten UTM-Parameter über eine moderne und benutzerfreundliche Oberfläche eingeben. Die Schnittstelle validiert die Eingaben, verknüpft sie entsprechend der Standards und generiert eine fertige Tracking-URL.
Das System geht nahtlos mit fehlenden oder zusätzlichen Parametern um und kodiert Sonderzeichen korrekt.

## Externe API-Nutzung

Diese Funktionalität steht auch als eigenständige REST-API zur Verfügung. Sie kann problemlos in externe Applikationen, CRM-Systeme, Marketing-Tools oder Skripte integriert werden, indem man einfache HTTP POST-Requests an den Endpunkt sendet.

**Endpoint:**
`POST /api/minimal-solutions/utm_link_builder`

**Headers:**
`Content-Type: application/json`

### Request-Beispiel (JSON)

```json
{
  "url": "https://example.com/product",
  "source": "newsletter",
  "medium": "email",
  "campaign": "spring_sale",
  "term": "running shoes",
  "content": "logo_link"
}
```

*Hinweis: Nur `url` und `source` sind Pflichtfelder. Die restlichen Parameter sind optional.*

### Response-Beispiel (JSON)

```json
{
  "status": "success",
  "data": {
    "utm_url": "https://example.com/product?utm_source=newsletter&utm_medium=email&utm_campaign=spring_sale&utm_term=running+shoes&utm_content=logo_link"
  }
}
```

### Fehlerbehandlung
Falls eine ungültige URL oder keine Source übergeben wird, liefert die API eine entsprechende Fehlermeldung:

```json
{
  "status": "error",
  "message": "Feld 'url' muss eine gültige URL sein."
}
```
