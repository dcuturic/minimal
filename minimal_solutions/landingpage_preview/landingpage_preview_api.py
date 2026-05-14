from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.landingpage_preview.landingpage_preview_validation import validate_preview_request

api_bp = Blueprint('landingpage_preview_api', __name__)

@api_bp.route('/api/minimal-solutions/landingpage_preview', methods=['POST'])
def landingpage_preview():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_preview_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    topic = data.get('topic')
    target = data.get('target')
    options = data.get('options', {})
    if isinstance(options, str):
        options = {"features": options}

    # Mocking a generated HTML preview
    tone = options.get('tone', 'professional')
    color = options.get('primary_color', '#10b981')
    features = options.get('features', '')
    
    features_html = f"<p style='color: #6b7280; font-size: 1.125rem; margin-bottom: 20px;'>Features: {features}</p>" if features else ""
    
    preview_html = f"""
    <div style="font-family: system-ui, sans-serif; max-width: 800px; margin: 0 auto; padding: 48px; text-align: center; background: #ffffff; border-radius: 12px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06); border: 1px solid #e5e7eb;">
        <h1 style="color: #111827; font-size: 3rem; font-weight: 800; letter-spacing: -0.025em; margin-bottom: 24px; line-height: 1.2;">{topic}</h1>
        <p style="color: #4b5563; font-size: 1.25rem; margin-bottom: 20px; line-height: 1.5; max-width: 600px; margin-left: auto; margin-right: auto;">Designed specifically for: <strong style="color: #111827;">{target}</strong></p>
        {features_html}
        <button style="background-color: {color}; color: white; padding: 16px 32px; border-radius: 8px; font-weight: 600; font-size: 1.125rem; border: none; cursor: pointer; transition: opacity 0.2s;">
            Get Started Now
        </button>
        <div style="margin-top: 48px; padding-top: 24px; border-top: 1px solid #e5e7eb; color: #9ca3af; font-size: 0.875rem;">
            Tone: {tone} | Auto-generated Preview
        </div>
    </div>
    """

    return success_response(data={
        "preview_html": preview_html,
        "meta": {
            "topic": topic,
            "target": target,
            "options": options
        }
    })
