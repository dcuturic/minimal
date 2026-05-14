from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.landingpage_builder.landingpage_builder_validation import validate_builder_request

api_bp = Blueprint('landingpage_builder_api', __name__)

@api_bp.route('/api/minimal-solutions/landingpage_builder', methods=['POST'])
def landingpage_builder():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_builder_request(data)
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

    # Generate builder result mock
    tone = options.get('tone', 'professional')
    color = options.get('primary_color', '#2563eb')
    features = options.get('features', '')

    builder_result = {
        "html": f'<div class="landing-page"><h1 style="color: {color}">{topic}</h1><p class="target-audience">For: {target}</p></div>',
        "css": f".landing-page {{ font-family: sans-serif; }} h1 {{ color: {color}; }}",
        "js": "console.log('Builder initialized');",
        "meta": {
            "tone": tone,
            "features": features
        }
    }

    return success_response(data={
        "builder_result": builder_result,
        "input": {
            "topic": topic,
            "target": target,
            "options": options
        }
    })
