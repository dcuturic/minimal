from app.validation import Validator

def validate_minecraft_checker_request(data):
    rules = {
        "input_text": {
            "required": True,
            "type": str,
            "min_length": 1,
            "max_length": 5000
        },
        "mode": {
            "required": True,
            "type": str,
            "min_length": 2,
            "max_length": 100
        },
        "options": {
            "required": False,
            "type": dict
        }
    }
    return Validator.validate(data, rules)
