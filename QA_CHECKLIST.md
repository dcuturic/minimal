# Minimal-Solution QA Checkliste (Global)

Diese globale QA-Checkliste stellt sicher, dass alle Minimal-Lösungen im CraftHoster-Projekt den gleichen hohen Qualitätsstandards entsprechen. Jede Minimal-Lösung muss diese Kriterien erfüllen, bevor sie als abgeschlossen gilt.

## 1. UI (User Interface)
- [ ] **Erreichbarkeit:** Die UI-Seite der Minimal-Lösung ist unter `/minimal-solutions/{identify}` erreichbar.
- [ ] **Integration:** Die Lösung ist auf der Übersichtsseite referenziert und verlinkt.
- [ ] **Empty States:** Wenn keine Daten vorhanden sind, wird der globale Empty-State angezeigt.
- [ ] **Loading States:** Bei API-Aufrufen oder Ladevorgängen werden globale Skeleton-Loader oder Lade-Indikatoren (Spinner/Lade-Buttons) genutzt.
- [ ] **Error Handling:** Tritt ein Fehler auf, wird das globale Error-Panel verwendet, um die Fehler-Informationen sauber darzustellen.
- [ ] **Global Action Components:** Falls anwendbar, werden standardisierte Copy-, Download- oder Export-Komponenten genutzt.

## 2. API (Backend)
- [ ] **Erreichbarkeit:** Der API-Endpunkt ist unter `/api/minimal-solutions/{identify}` erreichbar.
- [ ] **Response-Format:** Alle API-Antworten nutzen konsequent das Standard-Response-Format (`success_response` oder `error_response`).
- [ ] **Validierung:** Eingehende Daten werden über das globale Validierungssystem geprüft (inkl. Required, Type, Length).
- [ ] **Rate-Limiting:** Der Endpunkt ist durch die globale API Rate-Limit-Struktur geschützt.
- [ ] **Status-Codes:** Es werden korrekte HTTP-Status-Codes verwendet (z.B. 200, 201, 400, 404, 429, 500).

## 3. Dokumentation (Doku)
- [ ] **Ordnerstruktur:** Die Lösung befindet sich gekapselt im eigenen Ordner unter `minimal_solutions/{identify}`.
- [ ] **README.md:** Im Lösungs-Ordner existiert eine aktuelle und ausführliche `README.md`.
- [ ] **API-Dokumentation:** Auf der dynamischen Detailseite in der UI wird die API-Schnittstelle korrekt und vollständig dokumentiert (Endpoints, Methoden, Request-/Response-Beispiele).

## 4. Tests
- [ ] **Test-Datei:** Eine isolierte Test-Datei ist unter `tests/minimal_solutions/test_{identify}.py` angelegt.
- [ ] **Happy-Path:** Die erfolgreiche Standard-Ausführung (z.B. korrekte Eingabedaten) ist mit Tests abgedeckt.
- [ ] **Empty-Inputs:** Das Systemverhalten bei leeren oder unvollständigen Eingaben wird erfolgreich getestet.
- [ ] **Invalid Data:** Ungültige oder falsche Datenformate werden korrekt durch Validierungstests abgefangen (Error-Tests).

## 5. Design & Ästhetik
- [ ] **Monochrome Design System:** Die UI hält sich strikt an die vorgegebenen globalen Layout-Regeln und CSS-Variablen (Monochrome Ästhetik, Schwarz, Weiß, Grau).
- [ ] **Akzentfarbe:** Die leuchtende Primary-Akzentfarbe wird gezielt und subtil für wichtige Interaktionen oder dezente Glows genutzt.
- [ ] **Keine Stil-Brüche:** Es gibt keine fremden, nicht zum Design passenden Farben (z.B. zufälliges grelles Rot oder Blau ohne Systembezug) oder unpassende Layout-Brüche.
