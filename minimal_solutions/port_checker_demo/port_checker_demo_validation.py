from app.validation import Validator

def validate_port_checker_request(data):
    rules = {
        "host": {"required": True, "type": str},
        "port": {"required": True, "type": int}
    }

    is_valid, errors = Validator.validate(data, rules)
    
    if is_valid:
        host = data.get('host', '').strip()
        port = data.get('port')
        
        if not host:
            is_valid = False
            if 'host' not in errors:
                errors['host'] = []
            errors['host'].append("Der Host darf nicht leer sein.")
            
        if port < 1 or port > 65535:
            is_valid = False
            if 'port' not in errors:
                errors['port'] = []
            errors['port'].append("Der Port muss zwischen 1 und 65535 liegen.")
            
    return is_valid, errors
