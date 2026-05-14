from app.validation import Validator

def validate_request(data):
    rules = {
        "name": {
            "required": True,
            "type": str,
            "min_length": 1
        },
        "email": {
            "required": False,
            "type": str
        },
        "phone": {
            "required": False,
            "type": str
        },
        "company": {
            "required": False,
            "type": str
        },
        "address": {
            "required": False,
            "type": str
        }
    }
    
    is_valid, errors = Validator.validate(data, rules)
    return is_valid, errors
