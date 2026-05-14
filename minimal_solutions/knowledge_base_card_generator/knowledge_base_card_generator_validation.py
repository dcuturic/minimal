from app.validation import Validator

def validate_knowledge_base_card_generator_request(data):
    rules = {
        "source_text": {
            "required": True,
            "type": str,
            "min_length": 5
        },
        "category": {
            "required": False,
            "type": str
        }
    }
    return Validator.validate(data, rules)
