from app.validation import Validator

def validate_seo_analyzer_request(request_data: dict):
    rules = {
        "topic": {"required": True, "type": str, "min_length": 2},
        "target": {"required": False, "type": str},
        "options": {"required": False, "type": list}
    }
    return Validator.validate(request_data, rules)
