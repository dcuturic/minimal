from flask import Blueprint, jsonify, request
from .altersrechner_validation import validate_request
from app.responses import success_response, error_response, ErrorCodes
from datetime import datetime
import calendar

api_bp = Blueprint('altersrechner_api', __name__)

@api_bp.route('/api/minimal-solutions/altersrechner', methods=['POST'])
def calculate_age():
    data = request.get_json(silent=True) or {}
    
    is_valid, errors = validate_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )
        
    try:
        birth_dt = datetime.strptime(data["birth_date"], "%Y-%m-%d").date()
        if data.get("target_date"):
            target_dt = datetime.strptime(data["target_date"], "%Y-%m-%d").date()
        else:
            target_dt = datetime.today().date()
    except ValueError:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details={"_global": ["Ungültiges Datumsformat."]}
        )
        
    if target_dt < birth_dt:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details={"target_date": ["Das Ziel-Datum darf nicht in der Vergangenheit liegen (vor dem Geburtsdatum)."]}
        )

    # Totals
    total_days = (target_dt - birth_dt).days
    total_weeks = total_days // 7
    total_months = (target_dt.year - birth_dt.year) * 12 + target_dt.month - birth_dt.month
    if target_dt.day < birth_dt.day:
        total_months -= 1

    # Exact breakdown
    years = target_dt.year - birth_dt.year
    months = target_dt.month - birth_dt.month
    days = target_dt.day - birth_dt.day

    if days < 0:
        months -= 1
        prev_month = target_dt.month - 1 if target_dt.month > 1 else 12
        prev_year = target_dt.year if target_dt.month > 1 else target_dt.year - 1
        days_in_prev_month = calendar.monthrange(prev_year, prev_month)[1]
        days += days_in_prev_month

    if months < 0:
        years -= 1
        months += 12
        
    response_data = {
        "years": years,
        "months": months,
        "days": days,
        "total_days": total_days,
        "total_weeks": total_weeks,
        "total_months": max(0, total_months)
    }
    
    return success_response(data=response_data)
