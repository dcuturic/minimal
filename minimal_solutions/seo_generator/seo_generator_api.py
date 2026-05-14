from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from .seo_generator_validation import validate_request
import random

api_bp = Blueprint('seo_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/seo_generator', methods=['POST'])
def process():
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
    
    topic = data.get('topic')
    target = data.get('target')
    options = data.get('options', {})

    # Fake SEO generation logic for the minimal solution
    # In a real scenario, this might call an LLM or use advanced text processing
    
    language = options.get('language', 'de')
    tone = options.get('tone', 'professional')
    
    # Generate a meta title
    title_suffix = f" | {target}" if target else ""
    meta_title = f"{topic.capitalize()} - Best Practices & Guide{title_suffix}"
    
    if language == 'de':
        meta_title = f"{topic.capitalize()} - Der ultimative Guide{title_suffix}"
        
    # Generate a meta description
    if language == 'de':
        meta_description = f"Alles was Sie über {topic} für {target} wissen müssen. Tipps, Tricks und Strategien für {tone} Ergebnisse."
    else:
        meta_description = f"Everything you need to know about {topic} for {target}. Tips, tricks and strategies for {tone} results."
        
    # Generate keywords
    base_keywords = [topic.lower(), target.lower(), "guide", "tips", "strategy", "2026"]
    
    return success_response(data={
        "meta_title": meta_title[:60], # Recommended max length
        "meta_description": meta_description[:160], # Recommended max length
        "keywords": ", ".join([k for k in base_keywords if k])
    })
