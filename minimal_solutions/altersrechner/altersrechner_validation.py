from app.validation import Validator

def validate_request(data):
    rules = {
        "birth_date": {
            "required": True,
            "type": str,
            "format": (r'^\d{4}-\d{2}-\d{2}$', "YYYY-MM-DD")
        },
        "target_date": {
            "required": False,
            "type": str,
            "format": (r'^\d{4}-\d{2}-\d{2}$', "YYYY-MM-DD")
        }
    }
    
    is_valid, errors = Validator.validate(data, rules)
    return is_valid, errors
