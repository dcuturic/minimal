from app.validation import Validator

def validate_support_ticket_summarizer_request(data):
    rules = {
        "ticket_text": {
            "required": True,
            "type": str,
            "min_length": 1,
            "max_length": 50000
        }
    }
    return Validator.validate(data, rules)
