from app.validation import Validator

def validate_password_request(data):
    rules = {
        "length": {"required": True, "type": int},
        "use_numbers": {"required": True, "type": bool},
        "use_symbols": {"required": True, "type": bool},
        "use_uppercase": {"required": True, "type": bool}
    }

    is_valid, errors = Validator.validate(data, rules)
    
    if is_valid:
        length = data.get('length')
        if length < 4 or length > 128:
            is_valid = False
            errors['length'] = ["Das Passwort muss zwischen 4 und 128 Zeichen lang sein."]
            
    return is_valid, errors
