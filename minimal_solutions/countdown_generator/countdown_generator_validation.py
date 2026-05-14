from app.validation import Validator

def validate_request(data):
    rules = {
        "target_date": {
            "required": True,
            "type": str,
            "format": (r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(:\d{2})?(\.\d+)?$', "YYYY-MM-DDTHH:MM[:SS]")
        },
        "label": {
            "required": False,
            "type": str
        }
    }
    
    is_valid, errors = Validator.validate(data, rules)
    return is_valid, errors
