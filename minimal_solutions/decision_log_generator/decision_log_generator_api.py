from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.decision_log_generator.decision_log_generator_validation import validate_decision_log_request
import datetime

api_bp = Blueprint('decision_log_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/decision_log_generator', methods=['POST'])
def generate_decision_log():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_decision_log_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    context = data.get('context', '').strip()
    decision = data.get('decision', '').strip()
    reason = data.get('reason', '').strip()

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_content = (
        f"--- DECISION LOG ---\n"
        f"Date: {timestamp}\n"
        f"Context: {context}\n"
        f"Decision: {decision}\n"
        f"Reason: {reason}\n"
        f"--------------------"
    )

    return success_response(data={"log": log_content})
