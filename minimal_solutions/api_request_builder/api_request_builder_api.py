import json
from urllib.parse import urlparse
from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.api_request_builder.api_request_builder_validation import validate_api_request

api_bp = Blueprint('api_request_builder_api', __name__)

@api_bp.route('/api/minimal-solutions/api_request_builder', methods=['POST'])
def handle_api_request_builder():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_api_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    method = data.get('method', 'GET').upper()
    url = data.get('url', '')
    headers = data.get('headers') or {}
    body = data.get('body')
    
    # Generate curl preview
    curl_command = f"curl -X {method} '{url}'"
    
    for k, v in headers.items():
        curl_command += f" \\\n  -H '{k}: {v}'"
        
    if body is not None and method in ['POST', 'PUT', 'PATCH', 'DELETE']:
        if isinstance(body, (dict, list)):
            body_str = json.dumps(body)
            if "Content-Type" not in headers and "content-type" not in headers:
                curl_command += " \\\n  -H 'Content-Type: application/json'"
        else:
            body_str = str(body)
            
        # Escape single quotes for bash
        body_escaped = body_str.replace("'", "'\\''")
        curl_command += f" \\\n  -d '{body_escaped}'"
        
    # Generate Raw HTTP preview
    try:
        parsed_url = urlparse(url)
        path = parsed_url.path or "/"
        if parsed_url.query:
            path += "?" + parsed_url.query
            
        host = parsed_url.netloc
        
        raw_http = f"{method} {path} HTTP/1.1\nHost: {host}"
        for k, v in headers.items():
            raw_http += f"\n{k}: {v}"
            
        if body is not None and method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            if isinstance(body, (dict, list)):
                if "Content-Type" not in headers and "content-type" not in headers:
                    raw_http += "\nContent-Type: application/json"
                body_str = json.dumps(body, indent=2)
            else:
                body_str = str(body)
                
            raw_http += "\n\n" + body_str
    except Exception:
        raw_http = "Could not generate Raw HTTP preview due to URL parsing error."

    preview_text = f"=== cURL ===\n{curl_command}\n\n=== Raw HTTP ===\n{raw_http}"

    return success_response(data={
        "preview": preview_text,
        "curl": curl_command,
        "raw": raw_http
    })
