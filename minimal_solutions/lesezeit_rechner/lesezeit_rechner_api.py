from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.lesezeit_rechner.lesezeit_rechner_validation import validate_lesezeit_rechner_request
import math

api_bp = Blueprint('lesezeit_rechner_api', __name__)

@api_bp.route('/api/minimal-solutions/lesezeit_rechner', methods=['POST'])
def handle_lesezeit_rechner():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_lesezeit_rechner_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    text = data.get('text', '')
    words_per_minute = data.get('words_per_minute', 200)
    
    if isinstance(words_per_minute, str):
        try:
            words_per_minute = int(words_per_minute)
        except ValueError:
            words_per_minute = 200

    try:
        word_count = len(text.split())
        minutes = word_count / words_per_minute
        
        total_seconds = int(math.ceil(minutes * 60))
        calc_minutes = total_seconds // 60
        calc_seconds = total_seconds % 60
        
        if calc_minutes > 0:
            formatted_time = f"{calc_minutes} min {calc_seconds} sek"
        else:
            formatted_time = f"{calc_seconds} sek"
            
        return success_response(data={
            "result": formatted_time,
            "minutes": calc_minutes,
            "seconds": calc_seconds,
            "total_seconds": total_seconds,
            "word_count": word_count
        })
    except Exception as e:
        return error_response(
            code=ErrorCodes.INTERNAL_SERVER_ERROR,
            message="Interner Fehler beim Verarbeiten."
        )
