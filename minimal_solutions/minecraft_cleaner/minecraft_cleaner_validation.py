from app.validation import Validator

def validate_input(data):
    rules = {
        "input_text": {
            "required": True,
            "type": (str, list),
            "min_length": 1,
            "max_length": 5000
        },
        "mode": {
            "required": True,
            "type": str,
            "min_length": 1,
            "max_length": 50
        },
        "options": {
            "required": False,
            "type": dict
        }
    }
    return Validator.validate(data, rules)
