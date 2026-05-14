from app.validation import Validator

def validate_request(data):
    rules = {
        "topic": {
            "required": True,
            "type": str,
            "min_length": 3
        },
        "target": {
            "required": True,
            "type": str,
            "min_length": 3
        },
        "options": {
            "required": False,
            "type": dict
        }
    }
    return Validator.validate(data, rules)
