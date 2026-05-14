from app.validation import Validator

def validate_request(data):
    rules = {
        "start_date": {
            "required": True,
            "type": str,
            "format": (r'^\d{4}-\d{2}-\d{2}$', "YYYY-MM-DD")
        },
        "end_date": {
            "required": True,
            "type": str,
            "format": (r'^\d{4}-\d{2}-\d{2}$', "YYYY-MM-DD")
        }
    }
    
    is_valid, errors = Validator.validate(data, rules)
    return is_valid, errors
