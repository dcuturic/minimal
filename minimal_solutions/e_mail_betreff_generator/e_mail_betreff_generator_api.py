from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.e_mail_betreff_generator.e_mail_betreff_generator_validation import validate_e_mail_betreff_generator_input
import random

api_bp = Blueprint('e_mail_betreff_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/e_mail_betreff_generator', methods=['POST'])
def generate_email_subjects():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_e_mail_betreff_generator_input(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    topic = data.get('topic').strip()
    audience = data.get('audience').strip()
    tone = data.get('tone').strip()

    templates = [
        f"Der ultimative {topic} Guide für {audience}",
        f"Wie {audience} mit {topic} erfolgreich wird",
        f"Neu: {topic} - Exklusiv für {audience}",
        f"Verpassen Sie nicht unsere {topic} Tipps für {audience}",
        f"Die besten {topic} Strategien für {audience}"
    ]
    
    prefix = ""
    suffix = ""
    if tone.lower() in ['urgent', 'dringend']:
        prefix = "[WICHTIG] "
        suffix = " - Jetzt handeln!"
    elif tone.lower() in ['professional', 'professionell']:
        prefix = "Ihre Insights zu "
    elif tone.lower() in ['casual', 'locker', 'informell']:
        prefix = "Hey! "
        suffix = " 👀"
    elif tone.lower() in ['neugierig', 'curious']:
        prefix = "Haben Sie das über "
        suffix = " gewusst?"

    subjects = []
    for template in random.sample(templates, min(3, len(templates))):
        subjects.append(f"{prefix}{template}{suffix}")

    return success_response(data={"subjects": subjects})
