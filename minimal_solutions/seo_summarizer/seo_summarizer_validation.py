from app.validation import Validator

def validate_seo_summarizer_request(request_data: dict):
    rules = {
        "topic": {"required": True, "type": str, "min_length": 2},
        "target": {"required": True, "type": str, "min_length": 2},
        "options": {"required": False, "type": dict}
    }
    return Validator.validate(request_data, rules)
