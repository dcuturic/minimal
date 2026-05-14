from flask import Blueprint, request
from .image_prompt_generator_validation import validate_request
from app.responses import success_response, error_response, ErrorCodes

api_bp = Blueprint('image_prompt_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/image_prompt_generator', methods=['POST'])
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
    
    subject = data.get('subject', '').strip()
    style = data.get('style', '').strip()
    mood = data.get('mood', '').strip()
    aspect_ratio = data.get('aspect_ratio', '').strip()
    
    prompt = f"A high-quality image of {subject}, {style} style, {mood} mood, aspect ratio {aspect_ratio}, masterpiece, 8k resolution, highly detailed."
    
    return success_response({
        "prompt": prompt
    })
