from app.validation import Validator

def validate_mc_status_request(data):
    rules = {
        "host": {
            "required": True,
            "type": str,
        },
        "port": {
            "required": True,
            "type": int,
        }
    }
    
    is_valid, errors = Validator.validate(data, rules)
    return is_valid, errors
