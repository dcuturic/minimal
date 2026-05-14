from flask import Blueprint, jsonify, request
from .countdown_generator_validation import validate_request
from app.responses import success_response, error_response, ErrorCodes
from datetime import datetime

api_bp = Blueprint('countdown_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/countdown_generator', methods=['POST'])
def generate_countdown():
    data = request.get_json(silent=True) or {}
    
    is_valid, errors = validate_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )
        
    try:
        # datetime.fromisoformat can handle standard ISO formats like YYYY-MM-DDTHH:MM
        target = datetime.fromisoformat(data["target_date"])
        now = datetime.now()
    except ValueError:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details={"_global": ["Ungültiges Datumsformat. ISO 8601 Format erwartet."]}
        )
        
    if target <= now:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details={"target_date": ["Das Zieldatum muss in der Zukunft liegen."]}
        )

    diff = target - now
    days = diff.days
    hours, remainder = divmod(diff.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    label = data.get("label", "")
    title = label if label else "Countdown"
    
    response_data = {
        "title": title,
        "days": str(days).zfill(2),
        "hours": str(hours).zfill(2),
        "minutes": str(minutes).zfill(2),
        "seconds": str(seconds).zfill(2),
        "total_seconds": int(diff.total_seconds())
    }
    
    return success_response(data=response_data)
