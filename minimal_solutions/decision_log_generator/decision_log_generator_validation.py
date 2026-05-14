from app.validation import Validator

def validate_decision_log_request(data):
    rules = {
        "context": {"required": True, "type": str},
        "decision": {"required": True, "type": str},
        "reason": {"required": True, "type": str}
    }

    is_valid, errors = Validator.validate(data, rules)
    
    if is_valid:
        if not data.get('context', '').strip():
            is_valid = False
            errors['context'] = ["Der Kontext darf nicht leer sein."]
        if not data.get('decision', '').strip():
            is_valid = False
            errors['decision'] = ["Die Entscheidung darf nicht leer sein."]
        if not data.get('reason', '').strip():
            is_valid = False
            errors['reason'] = ["Die Begründung darf nicht leer sein."]
            
    return is_valid, errors
