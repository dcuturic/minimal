from app.validation import Validator

def validate_env_file_viewer_request(data):
    rules = {
        "env_text": {"required": True, "type": str}
    }
    
    is_valid, errors = Validator.validate(data, rules)
    return is_valid, errors
