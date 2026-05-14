# Validation for Testimonial Card Generator
from app.validation import Validator

def validate_testimonial_request(data):
    rules = {
        "name": {"required": True, "type": str},
        "role": {"required": True, "type": str},
        "quote": {"required": True, "type": str}
    }

    is_valid, errors = Validator.validate(data, rules)
    
    if is_valid:
        name = data.get('name', '').strip()
        role = data.get('role', '').strip()
        quote = data.get('quote', '').strip()
        
        if not name:
            is_valid = False
            errors['name'] = ["Das name Feld darf nicht leer sein."]
        elif len(name) > 100:
            is_valid = False
            errors['name'] = ["Das name Feld darf maximal 100 Zeichen lang sein."]
            
        if not role:
            is_valid = False
            errors['role'] = ["Das role Feld darf nicht leer sein."]
        elif len(role) > 100:
            is_valid = False
            errors['role'] = ["Das role Feld darf maximal 100 Zeichen lang sein."]
            
        if not quote:
            is_valid = False
            errors['quote'] = ["Das quote Feld darf nicht leer sein."]
        elif len(quote) > 1000:
            is_valid = False
            errors['quote'] = ["Das quote Feld darf maximal 1000 Zeichen lang sein."]
            
    return is_valid, errors
