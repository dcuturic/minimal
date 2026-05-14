# Validation logic for Social Post Formatter
from app.validation import Validator

def validate_post_request(data):
    rules = {
        "platform": {"required": True, "type": str},
        "text": {"required": True, "type": str}
    }

    is_valid, errors = Validator.validate(data, rules)
    
    if is_valid:
        platform = data.get('platform', '').strip().lower()
        allowed_platforms = ["twitter", "linkedin", "facebook", "instagram"]
        if platform not in allowed_platforms:
            is_valid = False
            errors['platform'] = [f"Ungültige platform. Erlaubt sind: {', '.join(allowed_platforms)}"]
            
        text = data.get('text', '').strip()
        if not text:
            is_valid = False
            errors['text'] = ["Der Text darf nicht leer sein."]
        elif len(text) > 10000:
            is_valid = False
            errors['text'] = ["Der Text darf maximal 10000 Zeichen lang sein."]
            
    return is_valid, errors
