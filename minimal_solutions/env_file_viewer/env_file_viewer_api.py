from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.env_file_viewer.env_file_viewer_validation import validate_env_file_viewer_request
import re

api_bp = Blueprint('env_file_viewer_api', __name__)

def is_secret_key(key):
    key_upper = key.upper()
    secret_keywords = ['SECRET', 'PASSWORD', 'PASS', 'TOKEN', 'KEY', 'AUTH', 'CREDENTIAL', 'API']
    for kw in secret_keywords:
        if kw in key_upper:
            return True
    return False

def mask_value(value):
    if len(value) <= 4:
        return '*' * len(value)
    return value[:2] + '*' * (len(value) - 4) + value[-2:]

@api_bp.route('/api/minimal-solutions/env_file_viewer', methods=['POST'])
def env_file_viewer():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt."
        )

    is_valid, errors = validate_env_file_viewer_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    env_text = data.get('env_text', '')
    
    parsed_env = []
    
    lines = env_text.split('\n')
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
            
        if '=' in line:
            parts = line.split('=', 1)
            key = parts[0].strip()
            value = parts[1].strip()
            
            if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
                value = value[1:-1]
            
            is_secret = is_secret_key(key)
            masked_value = mask_value(value) if is_secret else value
            
            parsed_env.append({
                "key": key,
                "value": masked_value,
                "is_secret": is_secret
            })

    return success_response(data={"parsed_env": parsed_env})
