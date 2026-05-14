from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.maintenance_page_generator.maintenance_page_generator_validation import validate_maintenance_page_generator_request

api_bp = Blueprint('maintenance_page_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/maintenance_page_generator', methods=['POST'])
def generate_maintenance_page():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_maintenance_page_generator_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    title = data.get('title')
    message = data.get('message')
    eta = data.get('eta')

    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: 'Inter', sans-serif;
            background-color: #0f0f0f;
            color: #ffffff;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            text-align: center;
        }}
        .container {{
            max-width: 600px;
            padding: 40px;
            background-color: #1a1a1a;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
            border: 1px solid #333;
        }}
        h1 {{
            font-size: 2.5rem;
            margin-bottom: 20px;
            color: #4a90e2;
        }}
        p {{
            font-size: 1.2rem;
            line-height: 1.6;
            margin-bottom: 30px;
            color: #cccccc;
        }}
        .eta {{
            display: inline-block;
            background-color: #2a2a2a;
            padding: 10px 20px;
            border-radius: 8px;
            font-weight: bold;
            font-size: 1.1rem;
            color: #e2a04a;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{title}</h1>
        <p>{message}</p>
        {'<div class="eta">Estimated Return: ' + eta + '</div>' if eta else ''}
    </div>
</body>
</html>"""

    return success_response(data={"html_output": html_template})
