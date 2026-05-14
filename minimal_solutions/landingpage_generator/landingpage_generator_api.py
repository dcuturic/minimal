from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.landingpage_generator.landingpage_generator_validation import validate_landingpage_generator_request

api_bp = Blueprint('landingpage_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/landingpage_generator', methods=['POST'])
def generate_landingpage():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_landingpage_generator_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    topic = data.get('topic', '').strip()
    target = data.get('target', '').strip()
    options = data.get('options', '').strip()
    
    # Generate landing page structure based on inputs
    landingpage_parts = []
    landingpage_parts.append(f"# Landingpage für: {topic}")
    landingpage_parts.append(f"**Zielgruppe / Target:** {target}\n")
    
    landingpage_parts.append("## 1. Hero Section")
    landingpage_parts.append(f"- **Headline:** Das ultimative Angebot für {target} rund um das Thema {topic}")
    landingpage_parts.append("- **Sub-Headline:** Entdecken Sie, wie Sie schnell und effizient Ihre Ziele erreichen.")
    landingpage_parts.append("- **Call to Action (CTA):** Jetzt kostenlos starten!\n")
    
    landingpage_parts.append("## 2. Problem & Lösung")
    landingpage_parts.append(f"- **Problem:** Viele {target} kämpfen mit Herausforderungen im Bereich {topic}.")
    landingpage_parts.append(f"- **Lösung:** Unsere Methode hilft, diese Hürden spielend zu meistern.\n")
    
    landingpage_parts.append("## 3. Features & Vorteile")
    landingpage_parts.append(f"- **Feature 1:** 100% fokussiert auf {topic}.")
    landingpage_parts.append(f"- **Feature 2:** Speziell zugeschnitten auf die Bedürfnisse von {target}.")
    landingpage_parts.append(f"- **Feature 3:** Einfach, schnell und effektiv.\n")
    
    if options:
        landingpage_parts.append("## 4. Zusatzoptionen (Options)")
        landingpage_parts.append(f"- {options}\n")
        
    landingpage_parts.append("## 5. Footer & Final CTA")
    landingpage_parts.append("- **Final CTA:** Warten Sie nicht länger, legen Sie heute noch los!")
    
    result = "\n".join(landingpage_parts).strip()

    return success_response(data={
        "result": result
    })
