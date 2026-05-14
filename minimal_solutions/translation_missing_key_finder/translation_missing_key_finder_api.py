from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.translation_missing_key_finder.translation_missing_key_finder_validation import validate_missing_key_request
import json

api = Blueprint('translation_missing_key_finder_api', __name__)

@api.route('/api/minimal-solutions/translation_missing_key_finder', methods=['POST'])
def find_missing_keys():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_missing_key_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    base_json = data.get('base_json')
    target_json = data.get('target_json')

    if isinstance(base_json, str):
        base_json = json.loads(base_json)
    if isinstance(target_json, str):
        target_json = json.loads(target_json)

    missing_keys = []

    def find_missing(base, target, prefix=""):
        for key, value in base.items():
            current_path = f"{prefix}.{key}" if prefix else key
            if key not in target:
                missing_keys.append(current_path)
            elif isinstance(value, dict) and isinstance(target[key], dict):
                find_missing(value, target[key], current_path)

    find_missing(base_json, target_json)

    return success_response(data={"missing_keys": missing_keys})
