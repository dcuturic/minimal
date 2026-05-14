from app.validation import Validator

def validate_rechnungsnummer_request(data):
    rules = {
        "prefix": {"required": True, "type": str},
        "year": {"required": True, "type": (int, str)},
        "start_number": {"required": True, "type": int},
        "count": {"required": True, "type": int}
    }

    is_valid, errors = Validator.validate(data, rules)
    
    if is_valid:
        count = int(data.get('count', 1))
        start_number = int(data.get('start_number', 1))
        
        if count < 1 or count > 500:
            is_valid = False
            errors['count'] = ["Die Anzahl muss zwischen 1 und 500 liegen."]
            
        if start_number < 1:
            is_valid = False
            errors['start_number'] = ["Die Startnummer muss größer als 0 sein."]
            
    return is_valid, errors
