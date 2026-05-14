from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.minecraft_motd_preview.minecraft_motd_preview_validation import validate_minecraft_motd_preview_request

api_bp = Blueprint('minecraft_motd_preview_api', __name__)

@api_bp.route('/api/minimal-solutions/minecraft_motd_preview', methods=['POST'])
def minecraft_motd_preview_api():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_minecraft_motd_preview_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )
    
    motd_text = data.get('motd_text')
    
    return success_response(data={
        "motd_text": motd_text
    })
