from app.validation import Validator

def validate_request(data):
    rules = {
        "title": {
            "required": True,
            "type": str,
            "min_length": 1,
            "max_length": 200
        },
        "summary": {
            "required": True,
            "type": str,
            "min_length": 1,
            "max_length": 2000
        },
        "links": {
            "required": False,
            "type": str,
            "max_length": 2000
        }
    }
    
    is_valid, errors = Validator.validate(data, rules)
            
    return is_valid, errors
