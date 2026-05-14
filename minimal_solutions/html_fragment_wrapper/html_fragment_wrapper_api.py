from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.html_fragment_wrapper.html_fragment_wrapper_validation import validate_html_fragment_wrapper_request

api_bp = Blueprint('html_fragment_wrapper_api', __name__)

@api_bp.route('/api/minimal-solutions/html_fragment_wrapper', methods=['POST'])
def handle_html_fragment_wrapper():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_html_fragment_wrapper_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    html = data.get('html', '')
    css = data.get('css', '')
    js = data.get('js', '')
    name = data.get('name', 'Wrapped Fragment')
    
    style_block = f"\n    <style>\n{css}\n    </style>" if css else ""
    script_block = f"\n    <script>\n{js}\n    </script>" if js else ""
    
    wrapped_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name}</title>{style_block}
</head>
<body>
{html}{script_block}
</body>
</html>"""

    return success_response(data={
        "wrapped_html": wrapped_html
    })
