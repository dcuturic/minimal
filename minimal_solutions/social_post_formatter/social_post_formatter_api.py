# API handler for Social Post Formatter
from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.social_post_formatter.social_post_formatter_validation import validate_post_request

api_bp = Blueprint('social_post_formatter_api', __name__)

@api_bp.route('/api/minimal-solutions/social_post_formatter', methods=['POST'])
def format_post():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_post_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    platform = data.get('platform', '').strip().lower()
    text = data.get('text', '').strip()
    
    result_text = text
    if platform == 'twitter':
        if len(result_text) > 260:
            result_text = result_text[:257] + "..."
        result_text += "\n\n#trending #now"
    elif platform == 'linkedin':
        result_text += "\n\n---\n#Business #Leadership #Professional"
    elif platform == 'facebook':
        result_text += "\n\n#Community #Updates"
    elif platform == 'instagram':
        result_text += "\n.\n.\n.\n#InstaGood #PhotoOfTheDay #Trending #Style #Inspiration"
        
    result = {
        "platform": platform,
        "formatted_text": result_text,
        "original_text": text
    }

    return success_response(data={"result": result})
