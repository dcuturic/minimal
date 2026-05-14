from app.validation import Validator

def validate_error_message_explainer_request(data):
    rules = {
        "error_text": {
            "required": True,
            "type": str,
            "min_length": 1,
            "max_length": 10000
        },
        "context": {
            "required": False,
            "type": str,
            "max_length": 10000
        }
    }
    return Validator.validate(data, rules)

