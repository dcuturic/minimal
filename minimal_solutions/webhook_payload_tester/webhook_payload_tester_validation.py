from app.validation import Validator

def validate_request(data):
    rules = {
        "payload_json": {
            "required": True,
            "type": str,
            "type_name": "String"
        }
    }
    return Validator.validate(data, rules)
