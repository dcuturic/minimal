from flask import Blueprint, request
from .datumsdifferenz_rechner_validation import validate_request
from app.responses import success_response, error_response, ErrorCodes
from datetime import datetime
import calendar

api_bp = Blueprint('datumsdifferenz_rechner_api', __name__)

@api_bp.route('/api/minimal-solutions/datumsdifferenz_rechner', methods=['POST'])
def calculate_date_difference():
    data = request.get_json(silent=True) or {}
    
    is_valid, errors = validate_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )
        
    try:
        start_dt = datetime.strptime(data["start_date"], "%Y-%m-%d").date()
        end_dt = datetime.strptime(data["end_date"], "%Y-%m-%d").date()
    except ValueError:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details={"_global": ["Ungültiges Datumsformat."]}
        )
        
    is_negative = end_dt < start_dt
    calc_start = end_dt if is_negative else start_dt
    calc_end = start_dt if is_negative else end_dt

    # Totals
    total_days = (calc_end - calc_start).days
    total_weeks = total_days / 7
    total_months = (calc_end.year - calc_start.year) * 12 + calc_end.month - calc_start.month
    if calc_end.day < calc_start.day:
        total_months -= 1

    # Exact breakdown
    years = calc_end.year - calc_start.year
    months = calc_end.month - calc_start.month
    days = calc_end.day - calc_start.day

    if days < 0:
        months -= 1
        prev_month = calc_end.month - 1 if calc_end.month > 1 else 12
        prev_year = calc_end.year if calc_end.month > 1 else calc_end.year - 1
        days_in_prev_month = calendar.monthrange(prev_year, prev_month)[1]
        days += days_in_prev_month

    if months < 0:
        years -= 1
        months += 12
        
    response_data = {
        "is_negative": is_negative,
        "total_days": total_days if not is_negative else -total_days,
        "total_weeks": round(total_weeks, 2) if not is_negative else -round(total_weeks, 2),
        "total_months": max(0, total_months) if not is_negative else -max(0, total_months),
        "breakdown": {
            "years": years,
            "months": months,
            "days": days
        }
    }
    
    return success_response(data=response_data)
