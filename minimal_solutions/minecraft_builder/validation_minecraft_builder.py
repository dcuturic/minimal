from app.validation import Validator

def validate_minecraft_builder_request(data):
    rules = {
        "input_text": {
            "required": True,
            "type": str,
            "min_length": 2,
            "max_length": 1000
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
