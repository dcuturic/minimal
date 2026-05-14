# Validation logic for Landingpage Section Generator
from app.validation import Validator

def validate_section_request(data):
    rules = {
        "section_type": {"required": True, "type": str},
        "topic": {"required": True, "type": str}
    }

    is_valid, errors = Validator.validate(data, rules)
    
    if is_valid:
        section_type = data.get('section_type', '').strip().lower()
        allowed_types = ["hero", "features", "testimonials", "cta", "faq"]
        if section_type not in allowed_types:
            is_valid = False
            errors['section_type'] = [f"Ungültiger section_type. Erlaubt sind: {', '.join(allowed_types)}"]
            
        topic = data.get('topic', '').strip()
        if not topic:
            is_valid = False
            errors['topic'] = ["Das topic darf nicht leer sein."]
        elif len(topic) > 200:
            is_valid = False
            errors['topic'] = ["Das topic darf maximal 200 Zeichen lang sein."]
            
    return is_valid, errors
