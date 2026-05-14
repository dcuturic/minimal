from app.validation import Validator

def validate_api_key_masker_request(data):
    rules = {
        "secret": {"required": True, "type": str},
        "visible_start": {"required": True, "type": int},
        "visible_end": {"required": True, "type": int}
    }

    is_valid, errors = Validator.validate(data, rules)
    
    if is_valid:
        visible_start = data.get('visible_start')
        visible_end = data.get('visible_end')
        
        if visible_start < 0:
            is_valid = False
            errors['visible_start'] = ["Der Wert darf nicht negativ sein."]
            
        if visible_end < 0:
            is_valid = False
            errors['visible_end'] = ["Der Wert darf nicht negativ sein."]
            
    return is_valid, errors
