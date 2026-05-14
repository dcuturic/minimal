from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.support_ticket_summarizer.support_ticket_summarizer_validation import validate_support_ticket_summarizer_request

api_bp = Blueprint('support_ticket_summarizer_api', __name__)

def summarize_ticket(text):
    text_lower = text.lower()
    
    problem = "Allgemeines Anliegen oder unbekanntes Problem."
    cause = "Konnte nicht automatisch ermittelt werden."
    next_steps = [
        "Bitte überprüfen Sie die Details im Ticket manuell.",
        "Kontaktieren Sie den Kunden für weitere Informationen."
    ]
    
    if "passwort" in text_lower or "password" in text_lower or "login" in text_lower:
        problem = "Kunde kann sich nicht einloggen oder hat sein Passwort vergessen."
        cause = "Passwort falsch oder Account gesperrt nach mehreren Fehlversuchen."
        next_steps = [
            "Senden Sie dem Kunden einen Link zum Zurücksetzen des Passworts.",
            "Überprüfen Sie den Account-Status im Admin-Panel."
        ]
    elif "server" in text_lower or "offline" in text_lower or "down" in text_lower or "absturz" in text_lower:
        problem = "Server des Kunden ist offline oder nicht erreichbar."
        cause = "Möglicherweise ein Netzwerkausfall, Wartungsarbeiten oder der Server ist abgestürzt."
        next_steps = [
            "Prüfen Sie den Server-Status im Monitoring-System.",
            "Starten Sie den Server gegebenenfalls neu.",
            "Informieren Sie den Kunden über den aktuellen Status."
        ]
    elif "rechnung" in text_lower or "bezahlen" in text_lower or "payment" in text_lower or "invoice" in text_lower:
        problem = "Frage oder Problem bezüglich einer Rechnung oder Zahlung."
        cause = "Zahlung fehlgeschlagen, unklare Abbuchung oder fehlende Rechnung."
        next_steps = [
            "Leiten Sie das Ticket an die Buchhaltung weiter.",
            "Überprüfen Sie den Zahlungsstatus im Billing-System."
        ]
        
    return {
        "problem": problem,
        "cause": cause,
        "next_steps": next_steps
    }

@api_bp.route('/api/minimal-solutions/support_ticket_summarizer', methods=['POST'])
def handle_support_ticket_summarizer():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt."
        )

    is_valid, errors = validate_support_ticket_summarizer_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )
        
    ticket_text = data.get('ticket_text', '')
    
    try:
        summary = summarize_ticket(ticket_text)
    except Exception:
        return error_response(
            code=ErrorCodes.INTERNAL_SERVER_ERROR,
            message="Interner Fehler beim Erstellen der Zusammenfassung."
        )
        
    return success_response(data=summary)
