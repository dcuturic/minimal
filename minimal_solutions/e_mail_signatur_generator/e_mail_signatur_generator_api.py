from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.e_mail_signatur_generator.e_mail_signatur_generator_validation import validate_request

api_bp = Blueprint('e_mail_signatur_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/e_mail_signatur_generator', methods=['POST'])
def handle_e_mail_signatur_generator():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    name = data.get('name', '').strip()
    role = data.get('role', '').strip()
    company = data.get('company', '').strip()
    email = data.get('email', '').strip()
    phone = data.get('phone', '').strip()
    website = data.get('website', '').strip()

    html = []
    html.append('<div style="font-family: Arial, sans-serif; font-size: 14px; color: #333333;">')
    html.append(f'<strong>{name}</strong>')

    if role and company:
        html.append(f'<br><span>{role} | {company}</span>')
    elif role:
        html.append(f'<br><span>{role}</span>')
    elif company:
        html.append(f'<br><span>{company}</span>')

    if email or phone or website:
        html.append('<br><br>')

    if email:
        html.append(f'<span>E-Mail: <a href="mailto:{email}" style="color: #0056b3;">{email}</a></span><br>')

    if phone:
        html.append(f'<span>Telefon: {phone}</span><br>')

    if website:
        website_url = website if website.startswith('http') else f'https://{website}'
        html.append(f'<span>Website: <a href="{website_url}" style="color: #0056b3;">{website}</a></span>')

    html.append('</div>')

    result = "".join(html)

    return success_response(data={
        "signature_html": result
    })
