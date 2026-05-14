from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.daily_plan_generator.daily_plan_generator_validation import validate_daily_plan_request

api_bp = Blueprint('daily_plan_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/daily_plan_generator', methods=['POST'])
def generate_daily_plan():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_daily_plan_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    tasks = data.get("tasks", [])
    available_hours = float(data.get("available_hours", 8.0))
    
    total_tasks = len(tasks)
    hours_per_task = available_hours / total_tasks
    
    plan = []
    current_hour = 9.0 # Start at 9:00 AM
    
    for task in tasks:
        start_time_str = f"{int(current_hour):02d}:{int((current_hour % 1) * 60):02d}"
        current_hour += hours_per_task
        end_time_str = f"{int(current_hour):02d}:{int((current_hour % 1) * 60):02d}"
        
        plan.append({
            "task": task,
            "duration_hours": round(hours_per_task, 2),
            "start_time": start_time_str,
            "end_time": end_time_str
        })
        
    return success_response(data={
        "plan": plan,
        "total_tasks": total_tasks,
        "available_hours": available_hours
    })
