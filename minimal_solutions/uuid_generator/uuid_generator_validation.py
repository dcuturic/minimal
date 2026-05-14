from app.validation import Validator

def validate_uuid_request(data):
    rules = {
        "count": {"required": True, "type": int},
        "version": {"required": True, "type": int}
    }

    is_valid, errors = Validator.validate(data, rules)
    
    if is_valid:
        count = data.get('count')
        version = data.get('version')
        
        if count < 1 or count > 500:
            is_valid = False
            errors['count'] = ["Die Anzahl muss zwischen 1 und 500 liegen."]
            
        if version not in [1, 3, 4, 5]:
            is_valid = False
            errors['version'] = ["Unterstützte UUID-Versionen sind 1, 3, 4 und 5."]
            
    return is_valid, errors
