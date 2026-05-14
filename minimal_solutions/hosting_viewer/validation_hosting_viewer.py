from app.validation import Validator

def validate_hosting_viewer_request(data):
    rules = {
        "source": {
            "required": True,
            "type": str,
            "min_length": 1
        },
        "config": {
            "required": False,
            "type": dict
        },
        "mode": {
            "required": True,
            "type": str,
            "min_length": 1
        }
    }
    return Validator.validate(data, rules)
