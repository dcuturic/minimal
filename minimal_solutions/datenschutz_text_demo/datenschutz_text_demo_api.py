# API für Datenschutz Text Demo
from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.datenschutz_text_demo.datenschutz_text_demo_validation import validate_datenschutz_request

api_bp = Blueprint('datenschutz_text_demo_api', __name__)

@api_bp.route('/api/minimal-solutions/datenschutz_text_demo', methods=['POST'])
def handle_datenschutz_text():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt."
        )

    is_valid, errors = validate_datenschutz_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    uses_cookies = data.get('uses_cookies')
    uses_analytics = data.get('uses_analytics')
    uses_contact_form = data.get('uses_contact_form')
    hosting_provider = data.get('hosting_provider', '').strip()
    
    text_parts = []
    text_parts.append("Datenschutzerklärung\n\n1. Allgemeines\nWir nehmen den Schutz Ihrer persönlichen Daten sehr ernst. Wir behandeln Ihre personenbezogenen Daten vertraulich und entsprechend der gesetzlichen Datenschutzvorschriften.")
    text_parts.append(f"2. Hosting\nWir hosten unsere Website bei: {hosting_provider}. Die Serverstandorte und Datenschutzrichtlinien dieses Anbieters sind für die Verarbeitung maßgeblich.")
    
    if uses_cookies:
        text_parts.append("3. Cookies\nUnsere Website verwendet Cookies. Das sind kleine Textdateien, die Ihr Webbrowser auf Ihrem Endgerät speichert. Cookies helfen uns dabei, unser Angebot nutzerfreundlicher, effektiver und sicherer zu machen.")
        
    if uses_analytics:
        text_parts.append("4. Analyse-Tools\nWir nutzen Analyse-Tools, um das Nutzerverhalten auszuwerten und unser Webangebot zu optimieren. Die Erfassung der Daten erfolgt in der Regel anonymisiert.")
        
    if uses_contact_form:
        text_parts.append("5. Kontaktformular\nWenn Sie uns per Kontaktformular Anfragen zukommen lassen, werden Ihre Angaben aus dem Anfrageformular inklusive der von Ihnen dort angegebenen Kontaktdaten zwecks Bearbeitung der Anfrage und für den Fall von Anschlussfragen bei uns gespeichert.")

    result = "\n\n".join(text_parts)

    return success_response(data={
        "result": result
    })
