from flask import Blueprint, request
from .youtube_description_generator_validation import validate_request
from app.responses import success_response, error_response, ErrorCodes

api_bp = Blueprint('youtube_description_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/youtube_description_generator', methods=['POST'])
def generate():
    data = request.get_json() or {}
    
    is_valid, errors = validate_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors,
            status_code=400
        )
    
    title = data.get('title', '').strip()
    summary = data.get('summary', '').strip()
    links = data.get('links', '')
    
    description_parts = []
    
    if title:
        description_parts.append(title)
        description_parts.append("-" * 20)
        
    if summary:
        description_parts.append(summary)
        description_parts.append("")
        
    if links and links.strip():
        description_parts.append("🔗 Links & Ressourcen:")
        for link in links.split('\n'):
            link = link.strip()
            if link:
                description_parts.append(f"• {link}")
        description_parts.append("")
        
    description_parts.append("📱 Folge mir:")
    description_parts.append("Instagram: @dein_account")
    description_parts.append("Twitter: @dein_account")
    description_parts.append("")
    description_parts.append("🔔 Vergiss nicht zu abonnieren und die Glocke zu aktivieren!")
    
    result = "\n".join(description_parts)
    
    return success_response({
        "description": result
    })
