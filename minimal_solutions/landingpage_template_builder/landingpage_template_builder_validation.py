from app.validation import Validator

def validate_template_builder_request(data):
    rules = {
        "topic": {"required": True, "type": str},
        "target": {"required": True, "type": str},
        "options": {"required": False, "type": str}
    }
    return Validator.validate(data, rules)
