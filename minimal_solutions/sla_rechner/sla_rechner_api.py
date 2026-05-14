from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.sla_rechner.sla_rechner_validation import validate_sla_request
from datetime import datetime, timedelta

api_bp = Blueprint('sla_rechner_api', __name__)

PRIORITY_MAP = {
    'p1': {'hours': 1, 'label': 'P1 - Critical'},
    'p2': {'hours': 4, 'label': 'P2 - High'},
    'p3': {'hours': 24, 'label': 'P3 - Medium'},
    'p4': {'hours': 48, 'label': 'P4 - Low'},
}

@api_bp.route('/api/minimal-solutions/sla_rechner', methods=['POST'])
def calculate_sla():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_sla_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    priority = data.get('priority')
    start_time_str = data.get('start_time')
    
    try:
        start_time = datetime.fromisoformat(start_time_str)
        priority_info = PRIORITY_MAP[priority]
        hours_to_add = priority_info['hours']
        
        deadline = start_time + timedelta(hours=hours_to_add)
        
        deadline_str = deadline.strftime('%Y-%m-%d %H:%M')
        
    except Exception as e:
        return error_response(
            code=ErrorCodes.INTERNAL_SERVER_ERROR,
            message="Interner Fehler beim Berechnen der SLA."
        )

    return success_response(data={
        "deadline": deadline_str,
        "priority_label": priority_info['label'],
        "time_remaining": f"{hours_to_add} Hours SLA"
    })
