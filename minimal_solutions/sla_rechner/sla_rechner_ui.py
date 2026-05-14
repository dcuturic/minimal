import os
from fasthtml.common import *

def get_ui():
    html_path = os.path.join(os.path.dirname(__file__), 'sla_rechner_component.html')
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
        
    return Div(
        NotStr(html_content),
        Div(
            H3("API-Dokumentation", cls="text-lg font-bold mb-4 text-white"),
            P("Die API ist unter folgendem Endpoint erreichbar:", cls="text-gray-400 text-sm mb-2"),
            Code("POST /api/minimal-solutions/sla_rechner", cls="block bg-gray-900 text-green-400 p-2 rounded mb-4"),
            H4("Request-Beispiel", cls="text-md font-semibold mb-2 text-gray-300"),
            Pre(Code("""{
  "priority": "p1",
  "start_time": "2026-05-12T08:00:00"
}""", cls="language-json"), cls="bg-gray-900 p-4 rounded mb-4 overflow-x-auto text-sm text-gray-300"),
            H4("Response-Beispiel", cls="text-md font-semibold mb-2 text-gray-300"),
            Pre(Code("""{
  "success": true,
  "data": {
    "deadline": "2026-05-12 09:00",
    "priority_label": "P1 - Critical",
    "time_remaining": "1 Hours SLA"
  }
}""", cls="language-json"), cls="bg-gray-900 p-4 rounded overflow-x-auto text-sm text-gray-300"),
            cls="api-doc-box mt-8 p-6 bg-gray-800 rounded-lg border border-gray-700"
        ),
        id="sla-rechner-ui",
        cls="minimal-solution-ui"
    )
