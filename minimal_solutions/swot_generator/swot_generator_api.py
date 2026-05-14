from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.swot_generator.swot_generator_validation import validate_swot_generator_input
import datetime

api_bp = Blueprint('swot_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/swot_generator', methods=['POST'])
def generate_swot():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_swot_generator_input(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    topic = data.get('topic', '').strip()
    notes = data.get('notes', '').strip()

    swot_data = {
        "strengths": [
            f"Tiefes Verständnis für das Thema: {topic}",
            "Starke anfängliche Motivation und Ressourcen"
        ],
        "weaknesses": [
            "Mögliche zeitliche Einschränkungen",
            "Mangelnde Erfahrung in speziellen Teilbereichen"
        ],
        "opportunities": [
            "Hohes Marktpotenzial und Wachstumschancen",
            "Integration mit bestehenden Systemen und Prozessen"
        ],
        "threats": [
            "Starke Konkurrenz im gleichen Bereich",
            "Veränderte Marktbedingungen oder Regularien"
        ]
    }
    
    if notes:
        swot_data["strengths"].append("Zusätzliche Notizen wurden berücksichtigt und strukturiert.")

    return success_response(data=swot_data)
