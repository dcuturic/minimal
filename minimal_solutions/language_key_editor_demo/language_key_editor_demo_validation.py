from app.validation import Validator

def validate_language_key_editor_request(data):
    rules = {
        "keys": {
            "required": True
        },
        "languages": {
            "required": True,
            "type": list
        }
    }
    return Validator.validate(data, rules)
