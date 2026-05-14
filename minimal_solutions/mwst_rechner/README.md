# MwSt Rechner

Minimal-Lösung für den MwSt Rechner.
Diese Lösung berechnet die Mehrwertsteuer (Netto zu Brutto oder Brutto zu Netto) auf Basis eines gegebenen Betrags und eines MwSt-Satzes.

## Externe Schnittstelle (API)

Du kannst diese Lösung als externe API in deinen eigenen Anwendungen nutzen.

**Endpoint:** `POST /api/minimal-solutions/mwst_rechner`

### Request-Beispiel

```json
{
  "amount": 100.0,
  "mode": "net_to_gross",
  "vat_rate": 19.0
}
```

- `amount` (float/int): Der Ausgangsbetrag.
- `mode` (string): Berechnungsart (`net_to_gross` oder `gross_to_net`).
- `vat_rate` (float/int): Der Mehrwertsteuersatz in Prozent (z.B. 19.0).

### Response-Beispiel

```json
{
  "status": "success",
  "data": {
    "net_amount": 100.0,
    "vat_amount": 19.0,
    "gross_amount": 119.0,
    "amount": 100.0,
    "mode": "net_to_gross",
    "vat_rate": 19.0
  }
}
```

- `net_amount`: Der berechnete oder gegebene Nettobetrag.
- `vat_amount`: Der berechnete Mehrwertsteuer-Betrag.
- `gross_amount`: Der berechnete oder gegebene Bruttobetrag.
