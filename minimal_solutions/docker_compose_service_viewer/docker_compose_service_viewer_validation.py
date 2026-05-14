from app.validation import Validator

def validate_docker_compose_service_viewer_request(data):
    rules = {
        "compose_yaml": {"required": True, "type": str}
    }
    
    is_valid, errors = Validator.validate(data, rules)
    return is_valid, errors
