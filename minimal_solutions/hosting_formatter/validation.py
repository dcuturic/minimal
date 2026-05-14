from app.validation import Validator

def validate_hosting_formatter_request(data: dict) -> tuple[bool, dict]:
    rules = {
        "source": {
            "required": True,
            "type": str
        },
        "config": {
            "required": True,
            "type": str
        },
        "mode": {
            "required": True,
            "type": str
        }
    }
    return Validator.validate(data, rules)
