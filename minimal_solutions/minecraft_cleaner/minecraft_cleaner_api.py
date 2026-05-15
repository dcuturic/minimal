from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from .minecraft_cleaner_validation import validate_input

api_bp = Blueprint('minecraft_cleaner_api', __name__)

@api_bp.route('/api/minimal-solutions/minecraft_cleaner', methods=['POST'])
def process():
    if not request.is_json:
        return error_response(ErrorCodes.BAD_REQUEST, "Request must be JSON")
    
    data = request.get_json()
    is_valid, errors = validate_input(data)
    
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors,
            status_code=400
        )
        
    input_text = data.get("input_text")
    mode = data.get("mode", "basic")
    options = data.get("options", {})
    
    remove_empty = options.get("remove_empty", False)

    import re
    # Minecraft color codes are usually § or & followed by 0-9, a-f, k-o, r
    pattern = r'[&§][0-9a-fA-Fk-oK-oRr]'
    
    def clean_text(text, m):
        cleaned = re.sub(pattern, '', str(text))
        if m == 'strict':
            # Strict mode: also strip non-printable characters or excessive whitespace
            cleaned = re.sub(r'[^A-Za-z0-9_\-\. ]+', '', cleaned)
            cleaned = cleaned.strip()
        return cleaned

    if isinstance(input_text, list):
        cleaned_list = [clean_text(item, mode) for item in input_text]
        if remove_empty:
            cleaned_list = [item for item in cleaned_list if item.strip() != ""]
        result_data = {
            "input_text": cleaned_list,
            "mode": mode,
            "options": options,
            "message": "Clean erfolgreich durchgeführt."
        }
    else:
        cleaned_str = clean_text(input_text, mode)
        if remove_empty and cleaned_str.strip() == "":
            cleaned_str = ""
        result_data = {
            "input_text": cleaned_str,
            "mode": mode,
            "options": options,
            "message": "Clean erfolgreich durchgeführt."
        }
    
    return success_response(data=result_data)
