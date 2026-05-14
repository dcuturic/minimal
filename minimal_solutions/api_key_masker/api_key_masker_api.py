from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.api_key_masker.api_key_masker_validation import validate_api_key_masker_request

api_bp = Blueprint('api_key_masker_api', __name__)

@api_bp.route('/api/minimal-solutions/api_key_masker', methods=['POST'])
def mask_api_key():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_api_key_masker_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    secret = data.get('secret')
    visible_start = data.get('visible_start', 0)
    visible_end = data.get('visible_end', 0)

    length = len(secret)

    if visible_start + visible_end >= length:
        masked = secret
    else:
        start_part = secret[:visible_start] if visible_start > 0 else ""
        end_part = secret[-visible_end:] if visible_end > 0 else ""
        mask_length = length - visible_start - visible_end
        masked = f"{start_part}{'*' * mask_length}{end_part}"

    return success_response(data={"result": masked, "masked_key": masked})
