from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.time_estimation_calculator.time_estimation_calculator_validation import validate_time_estimation_request

api_bp = Blueprint('time_estimation_calculator_api', __name__)

@api_bp.route('/api/minimal-solutions/time_estimation_calculator', methods=['POST'])
def calculate_time_estimation():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_time_estimation_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    ticket_count = float(data['ticket_count'])
    minutes_per_ticket = float(data['minutes_per_ticket'])
    days = float(data['days'])
    workers = float(data['workers'])

    req_min = ticket_count * minutes_per_ticket
    cap_min = days * workers * 8 * 60
    
    total_hours_required = round(req_min / 60, 2)
    total_hours_available = round(cap_min / 60, 2)
    
    is_feasible = req_min <= cap_min
    
    cap_min_safe = cap_min if cap_min > 0 else 1
    utilization_percent = round((req_min / cap_min_safe) * 100, 2)

    return success_response(data={
        "total_hours_required": total_hours_required,
        "total_hours_available": total_hours_available,
        "is_feasible": is_feasible,
        "utilization_percent": utilization_percent
    })
