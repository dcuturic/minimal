from app.validation import Validator

def validate_utm_link_builder_input(data):
    rules = {
        "url": {
            "required": True,
            "type": str,
            "max_length": 2048,
            "format": (r'^https?://.+', "Gültige URL (http/https)")
        },
        "source": {
            "required": True,
            "type": str,
            "max_length": 255
        },
        "medium": {
            "required": True,
            "type": str,
            "max_length": 255
        },
        "campaign": {
            "required": True,
            "type": str,
            "max_length": 255
        },
        "term": {
            "required": False,
            "type": str,
            "max_length": 255
        },
        "content": {
            "required": False,
            "type": str,
            "max_length": 255
        }
    }
    
    is_valid, errors = Validator.validate(data, rules)
    return is_valid, errors
