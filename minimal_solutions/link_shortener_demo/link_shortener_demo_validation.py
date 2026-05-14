from app.validation import Validator

def validate_link_shortener_request(data):
    rules = {
        "long_url": {
            "required": True,
            "type": str,
            "format": (r'^https?://.*$', "Gültige URL (http:// oder https://)")
        },
        "custom_slug": {
            "required": False,
            "type": str,
            "max_length": 50,
            "format": (r'^[a-zA-Z0-9_-]*$', "Alphanumerisch mit Binde-/Unterstrich")
        }
    }
    return Validator.validate(data, rules)
