from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.landingpage_analyzer.landingpage_analyzer_validation import validate_analyzer_request

api_bp = Blueprint('landingpage_analyzer_api', __name__)

@api_bp.route('/api/minimal-solutions/landingpage_analyzer', methods=['POST'])
def landingpage_analyzer():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_analyzer_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    topic = data.get('topic')
    target = data.get('target')
    options = data.get('options', '')

    # Dummy analysis logic
    analysis = {
        "score": 85,
        "strengths": [
            f"Topic '{topic}' is highly relevant.",
            f"Target audience '{target}' is well-defined."
        ],
        "weaknesses": [
            "Consider adding more specific options." if not options else "Options could be more detailed."
        ],
        "recommendations": [
            "Use clear and concise language.",
            "Add a strong call to action."
        ]
    }

    return success_response(data={
        "analysis_result": analysis,
        "meta": {
            "topic": topic,
            "target": target,
            "options": options
        }
    })
