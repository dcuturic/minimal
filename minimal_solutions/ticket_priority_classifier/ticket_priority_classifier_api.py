from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.ticket_priority_classifier.ticket_priority_classifier_validation import validate_priority_request
import re

api_bp = Blueprint('ticket_priority_classifier_api', __name__)

def classify_priority(text: str) -> str:
    text_lower = text.lower()
    
    high_keywords = ['dringend', 'urgent', 'notfall', 'ausfall', 'down', 'kaputt', 'crash', 'kritisch', 'sofort', 'offline', 'fatal']
    medium_keywords = ['bug', 'fehler', 'problem', 'hilfe', 'error', 'geht nicht', 'funktioniert nicht', 'wichtig']
    
    if any(keyword in text_lower for keyword in high_keywords):
        return 'Hoch'
    elif any(keyword in text_lower for keyword in medium_keywords):
        return 'Mittel'
    else:
        return 'Niedrig'

@api_bp.route('/api/minimal-solutions/ticket_priority_classifier', methods=['POST'])
def handle_ticket_priority_classifier():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_priority_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    ticket_text = data.get('ticket_text')
    
    try:
        priority = classify_priority(ticket_text)
        
        # Simple rationale generation
        rationale = "Klassifiziert basierend auf Schlüsselwörtern im Ticket-Text."
        if priority == 'Hoch':
            rationale = "Kritische Schlüsselwörter erkannt (z.B. dringend, ausfall, notfall)."
        elif priority == 'Mittel':
            rationale = "Fehler-relevante Schlüsselwörter erkannt (z.B. fehler, problem, bug)."
        else:
            rationale = "Keine kritischen oder fehler-relevanten Schlüsselwörter gefunden, Standardpriorität."
            
    except Exception:
        return error_response(
            code=ErrorCodes.INTERNAL_SERVER_ERROR,
            message="Interner Fehler beim Verarbeiten."
        )

    return success_response(data={
        "priority": priority,
        "rationale": rationale
    })
