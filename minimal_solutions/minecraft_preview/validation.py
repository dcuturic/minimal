from app.validation import Validator

def validate_minecraft_preview_request(data):
    rules = {
        "input_text": {
            "required": True,
            "type": str
        },
        "mode": {
            "required": True,
            "type": str
        },
        "options": {
            "required": False,
            "type": dict
        }
    }
    return Validator.validate(data, rules)
