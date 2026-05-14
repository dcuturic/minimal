from app.validation import Validator

def validate_request(data):
    rules = {
        "topic": {
            "required": True,
            "type": str,
            "min_length": 1,
            "max_length": 100
        },
        "audience": {
            "required": True,
            "type": str,
            "min_length": 1,
            "max_length": 100
        }
    }
    
    is_valid, errors = Validator.validate(data, rules)
    
    if is_valid:
        count = data.get('count', 10)
        try:
            count = int(count)
            if count < 1 or count > 100:
                is_valid = False
                errors['count'] = ["Die Anzahl muss zwischen 1 und 100 liegen."]
        except (ValueError, TypeError):
            is_valid = False
            errors['count'] = ["Die Anzahl muss eine gültige Zahl sein."]
            
    return is_valid, errors
