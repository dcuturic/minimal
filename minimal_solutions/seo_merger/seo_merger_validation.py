from app.validation import Validator

def validate_seo_merger_request(data):
    rules = {
        "topic": {
            "required": True,
            "type": str,
            "min_length": 2,
            "max_length": 200
        },
        "target": {
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
