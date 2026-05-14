# CraftHoster Minimal Solutions Platform

## Globales Testmuster
Jede Minimal-Lösung in dieser Plattform muss das folgende Testmuster implementieren, um Qualität und Konsistenz zu gewährleisten:

1. **Happy-Path:** Testet das normale Verhalten der API oder UI mit gültigen Daten. Es wird ein Erfolgsstatus (z.B. 200 OK) und die erwartete Antwort erwartet.
2. **Empty-Input:** Testet das Verhalten der API bei leeren Eingaben (z.B. fehlende Pflichtfelder). Es wird erwartet, dass das System kontrolliert reagiert und sinnvolle Fehlermeldungen (z.B. über das globale Validierungssystem) liefert.
3. **Invalid-Input:** Testet das Verhalten der API bei ungültigen Daten (falsches Format, falscher Typ). Das System soll eine definierte Fehler-Antwort (z.B. 400 Bad Request) zurückgeben.

Ein Beispieltest ist unter `tests/minimal_solutions/test_example.py` zu finden. Der Skript-Generator (`generate_solution.py`) erstellt standardmäßig Test-Stubs für dieses Muster.
# minimal
