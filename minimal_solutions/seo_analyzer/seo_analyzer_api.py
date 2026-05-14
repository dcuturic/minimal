from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.seo_analyzer.seo_analyzer_validation import validate_seo_analyzer_request

api_bp = Blueprint('seo_analyzer_api', __name__)

@api_bp.route('/api/minimal-solutions/seo_analyzer', methods=['POST'])
def handle_seo_analyzer_request():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_seo_analyzer_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    topic = data.get("topic", "")
    target = data.get("target", "Allgemein")
    options = data.get("options", [])
    
    score = 85
    issues = []
    
    if len(topic) < 10:
        score -= 20
        issues.append("Die Eingabe (Topic) ist sehr kurz. Etwas mehr Text oder eine vollständige URL wird empfohlen.")
        
    keyword_density = "N/A"
    if "check_density" in options:
        keyword_density = "2.5%"

    analysis_result = {
        "score": score,
        "issues": issues,
        "keyword_density": keyword_density
    }

    return success_response(data=analysis_result)
