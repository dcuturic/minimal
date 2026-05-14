from flask import Blueprint, request
from .tiktok_caption_generator_validation import validate_request
from app.responses import success_response, error_response, ErrorCodes

api_bp = Blueprint('tiktok_caption_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/tiktok_caption_generator', methods=['POST'])
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
    tone = data.get('tone', '').strip()
    
    caption_parts = []
    tone_lower = tone.lower()
    topic_tag = "".join(e for e in topic if e.isalnum())
    if not topic_tag:
        topic_tag = "tiktok"
    
    if "lustig" in tone_lower or "funny" in tone_lower or "humor" in tone_lower or "witzig" in tone_lower:
        caption_parts.append(f"POV: Du probierst {topic} und es eskaliert komplett! 😂😭")
        caption_parts.append("Wer kennt das auch? Markiert jemanden, der genau so ist!")
        caption_parts.append("")
        caption_parts.append(f"#funny #comedy #relatable #{topic_tag}")
    elif "seriös" in tone_lower or "serious" in tone_lower or "informativ" in tone_lower:
        caption_parts.append(f"Wusstest du schon das Wichtigste über {topic}?")
        caption_parts.append("Hier sind spannende Fakten, die dir helfen können. Speichere das Video für später!")
        caption_parts.append("")
        caption_parts.append(f"#wissen #informativ #tipps #{topic_tag}")
    elif "provokant" in tone_lower or "edgy" in tone_lower or "kontrovers" in tone_lower:
        caption_parts.append(f"Warum {topic} komplett überbewertet ist... Change my mind. ☕️👀")
        caption_parts.append("Lass uns in den Kommentaren diskutieren!")
        caption_parts.append("")
        caption_parts.append(f"#meinung #diskussion #hoteltake #{topic_tag}")
    elif "motivierend" in tone_lower or "motivational" in tone_lower:
        caption_parts.append(f"Lass dich nicht aufhalten! Hier ist deine tägliche Dosis {topic}. 💪✨")
        caption_parts.append("Glaube an dich und zieh durch!")
        caption_parts.append("")
        caption_parts.append(f"#motivation #mindset #erfolg #{topic_tag}")
    else:
        caption_parts.append(f"Hier ist mein neuer Beitrag zum Thema {topic}! ✨")
        caption_parts.append(f"Stimmung des Tages: {tone}. Was denkt ihr darüber?")
        caption_parts.append("")
        caption_parts.append(f"#{topic_tag} #fyp #foryou")

    result = "\n".join(caption_parts)
    
    return success_response({
        "caption": result
    })
