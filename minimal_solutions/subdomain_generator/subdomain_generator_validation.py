from app.validation import Validator

def validate_subdomain_request(data):
    rules = {
        "name": {"required": True, "type": str},
        "base_domain": {"required": True, "type": str}
    }
    
    is_valid, errors = Validator.validate(data, rules)
    
    if is_valid:
        if not data.get("name").strip():
            is_valid = False
            errors["name"] = ["Der Name darf nicht leer sein."]
        if not data.get("base_domain").strip():
            is_valid = False
            errors["base_domain"] = ["Die Basis-Domain darf nicht leer sein."]
            
    return is_valid, errors
