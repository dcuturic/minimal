import re
from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.error_message_explainer.error_message_explainer_validation import validate_error_message_explainer_request

api_bp = Blueprint('error_message_explainer_api', __name__)

def generate_explanation(error_text, context):
    # Mock behavior based on common error patterns
    error_lower = error_text.lower()
    
    causes = []
    resolution_steps = []
    
    if "syntaxerror" in error_lower or "syntax error" in error_lower:
        causes.append("Im Code gibt es einen Tippfehler oder ein fehlendes Zeichen (z.B. Komma, Klammer, Doppelpunkt).")
        resolution_steps.append("Überprüfen Sie die angegebene Zeile auf fehlende Zeichen.")
        resolution_steps.append("Achten Sie auf korrekte Einrückung und Klammersetzung.")
    elif "nullpointer" in error_lower or "nonetype" in error_lower or "undefined" in error_lower:
        causes.append("Es wird versucht auf eine Variable oder ein Objekt zuzugreifen, das nicht initialisiert wurde (Null / None / Undefined).")
        resolution_steps.append("Stellen Sie sicher, dass das Objekt korrekt erstellt wurde, bevor Sie darauf zugreifen.")
        resolution_steps.append("Fügen Sie Checks ein (z.B. 'if object is not None:').")
    elif "connection refused" in error_lower or "timeout" in error_lower or "econnrefused" in error_lower:
        causes.append("Die Verbindung zum Zielserver konnte nicht hergestellt werden (Server down, falscher Port, Firewall).")
        resolution_steps.append("Prüfen Sie, ob der Zielserver läuft und erreichbar ist.")
        resolution_steps.append("Überprüfen Sie Hostname und Port auf Tippfehler.")
    else:
        causes.append("Ein allgemeiner Fehler ist aufgetreten. Die genaue Ursache konnte nicht automatisch bestimmt werden.")
        resolution_steps.append("Suchen Sie nach dem Fehlercode in der Dokumentation des verwendeten Frameworks.")
        resolution_steps.append("Prüfen Sie die Log-Dateien auf vorhergehende Warnungen.")
        
    return {
        "causes": causes,
        "resolution_steps": resolution_steps
    }

@api_bp.route('/api/minimal-solutions/error_message_explainer', methods=['POST'])
def handle_error_message_explainer():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_error_message_explainer_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )
        
    error_text = data.get('error_text', '')
    context = data.get('context', '')
    
    try:
        explanation = generate_explanation(error_text, context)
    except Exception:
        return error_response(
            code=ErrorCodes.INTERNAL_SERVER_ERROR,
            message="Interner Fehler beim Verarbeiten."
        )
        
    return success_response(data=explanation)
