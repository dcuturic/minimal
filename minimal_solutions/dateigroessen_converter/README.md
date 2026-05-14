# Dateigrößen Converter

Der **Dateigrößen Converter** ist eine Minimal-Lösung, mit der man Dateigrößen zwischen verschiedenen Einheiten (Bytes, KB, MB, GB, TB) konvertieren kann.

## API-Nutzung (Schnittstelle)

Die Lösung bietet eine REST-API, die extern angesprochen werden kann. Alle Anfragen müssen als `POST` an den entsprechenden Endpoint geschickt werden und als `Content-Type: application/json` formatiert sein.

### Endpoint

`POST /api/minimal-solutions/dateigroessen_converter`

### Request (Beispiel)

```json
{
    "value": 1024,
    "from_unit": "MB",
    "to_unit": "GB"
}
```

* `value` (Number): Der Wert, der konvertiert werden soll.
* `from_unit` (String): Die Einheit des Wertes (z.B. "B", "KB", "MB", "GB", "TB").
* `to_unit` (String): Die Zieleinheit, in die konvertiert werden soll.

### Response (Beispiel)

```json
{
    "status": "success",
    "data": {
        "result": 1.024,
        "formatted": "1.02 GB"
    }
}
```

* `status`: Gibt an, ob die Anfrage erfolgreich war ("success" oder "error").
* `data.result`: Das genaue, numerische Ergebnis der Konvertierung.
* `data.formatted`: Ein formatiertes String-Ergebnis (auf zwei Nachkommastellen gerundet und mit Einheit versehen).
