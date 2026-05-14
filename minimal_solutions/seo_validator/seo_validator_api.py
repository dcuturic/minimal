from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from .seo_validator_validation import validate_request

api_bp = Blueprint('seo_validator_api', __name__)

@api_bp.route('/api/minimal-solutions/seo_validator', methods=['POST'])
def process():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )
    
    topic = data.get('topic')
    target = data.get('target')
    options = data.get('options', {})

    # Fake SEO validation logic
    score = 85
    issues = []
    if len(topic) < 5:
        score -= 20
        issues.append("Topic is too short.")
    if len(target) < 5:
        score -= 10
        issues.append("Target is too short.")
        
    recommendations = ["Add more LSI keywords", "Improve meta description length"]
    
    if score == 85:
        issues.append("No major issues found.")

    return success_response(data={
        "score": score,
        "issues": issues,
        "recommendations": recommendations,
        "status": "valid" if score >= 80 else "needs_improvement"
    })
