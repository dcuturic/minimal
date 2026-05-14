from flask import Blueprint, request
from .tts_script_generator_validation import validate_request
from app.responses import success_response, error_response, ErrorCodes

api_bp = Blueprint('tts_script_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/tts_script_generator', methods=['POST'])
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
    
    topic = data.get('topic', '').strip()
    voice_style = data.get('voice_style', '').strip()
    duration = data.get('duration', '').strip()
    
    style_lower = voice_style.lower()
    
    script_intro = f"Willkommen zu unserem heutigen Video über {topic}!"
    if "dramatisch" in style_lower or "dramatic" in style_lower:
        script_intro = f"Eine Welt im Wandel. Heute enthüllen wir die Wahrheit über {topic}."
    elif "lustig" in style_lower or "funny" in style_lower or "humorvoll" in style_lower:
        script_intro = f"Achtung, Lachmuskeln festhalten! Heute geht's um {topic}."
    elif "seriös" in style_lower or "serious" in style_lower:
        script_intro = f"Guten Tag. In diesem Beitrag analysieren wir {topic}."
        
    script_body = f"Dieses {duration} Video wird dir alles erklären, was du über {topic} wissen musst. Bleib dran und pass genau auf, denn diese Informationen sind Gold wert."
    script_outro = "Danke fürs Zuschauen! Vergiss nicht, ein Abo dazulassen und dieses Video zu teilen."
    
    script = f"{script_intro}\n\n{script_body}\n\n{script_outro}"
    
    return success_response({
        "script": script
    })
