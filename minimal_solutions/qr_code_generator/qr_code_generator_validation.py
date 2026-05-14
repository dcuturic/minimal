from app.validation import Validator

def validate_qr_code_generator_input(data):
    rules = {
        "text": {"type": str, "max_length": 2048},
        "url": {"type": str, "max_length": 2048},
        "wifi_ssid": {"type": str, "max_length": 255},
        "wifi_password": {"type": str, "max_length": 255}
    }
    is_valid, errors = Validator.validate(data, rules)
    
    # Custom validation to ensure at least one payload is provided
    if is_valid:
        if not any([data.get('text'), data.get('url'), data.get('wifi_ssid')]):
            is_valid = False
            errors['_global'] = ["Bitte mindestens 'text', 'url' oder 'wifi_ssid' angeben."]

    return is_valid, errors
