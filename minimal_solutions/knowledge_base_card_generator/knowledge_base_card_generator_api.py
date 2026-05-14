from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.knowledge_base_card_generator.knowledge_base_card_generator_validation import validate_knowledge_base_card_generator_request
import re

api_bp = Blueprint('knowledge_base_card_generator_api', __name__)

def generate_kb_card(text, category):
    title_words = text.split()[:5]
    title = " ".join(title_words) + ("..." if len(text.split()) > 5 else "")
    summary = text[:150] + ("..." if len(text) > 150 else "")
    
    sentences = [s.strip() for s in re.split(r'[.!?\n]', text) if len(s.strip()) > 10]
    key_points = sentences[:3] if sentences else [summary]
    
    card = {
        "title": title.title(),
        "summary": summary,
        "category": category if category else "Uncategorized",
        "key_points": key_points
    }
    return card

@api_bp.route('/api/minimal-solutions/knowledge_base_card_generator', methods=['POST'])
def handle_knowledge_base_card_generator():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_knowledge_base_card_generator_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )
        
    source_text = data.get('source_text', '')
    category = data.get('category', '')
    
    try:
        card = generate_kb_card(source_text, category)
    except Exception as e:
        return error_response(
            code=ErrorCodes.INTERNAL_SERVER_ERROR,
            message="Interner Fehler beim Generieren der Knowledge Base Card."
        )
        
    return success_response(data={"card": card})
