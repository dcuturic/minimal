from app.validation import Validator

def validate_request(data):
    rules = {
        "topic": {
            "required": True,
            "type": str,
            "min_length": 1,
            "max_length": 500
        },
        "tone": {
            "required": True,
            "type": str,
            "min_length": 1,
            "max_length": 100
        }
    }
    
    is_valid, errors = Validator.validate(data, rules)
            
    return is_valid, errors
