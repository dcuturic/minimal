from app.validation import Validator

def validate_docker_card_request(data):
    rules = {
        "name": {
            "required": True,
            "type": str,
        },
        "status": {
            "required": True,
            "type": str,
        },
        "image": {
            "required": True,
            "type": str,
        },
        "ports": {
            "required": True,
        }
    }
    
    is_valid, errors = Validator.validate(data, rules)
    return is_valid, errors
