from app.validation import Validator

def validate_iframe_preview_url_builder_request(data):
    rules = {
        "page": {
            "required": True,
            "type": str,
            "min_length": 1
        },
        "component": {
            "required": True,
            "type": str,
            "min_length": 1
        },
        "mode": {
            "required": False,
            "type": str
        }
    }
    return Validator.validate(data, rules)
