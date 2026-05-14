def validate_missing_key_request(data):
    errors = []
    
    if not isinstance(data, dict):
        return False, ["Erwartet wurde ein JSON-Objekt/Dictionary."]
        
    if 'base_json' not in data:
        errors.append("Feld 'base_json' fehlt.")
    if 'target_json' not in data:
        errors.append("Feld 'target_json' fehlt.")
        
    if errors:
        return False, errors
        
    base = data.get('base_json')
    target = data.get('target_json')
    
    import json
    
    def _parse(val, name):
        if isinstance(val, dict):
            return True
        elif isinstance(val, str):
            try:
                parsed = json.loads(val)
                if not isinstance(parsed, dict):
                    errors.append(f"{name} muss ein JSON-Objekt (Dictionary) sein.")
                    return False
                return True
            except json.JSONDecodeError:
                errors.append(f"{name} ist kein gültiges JSON.")
                return False
        else:
            errors.append(f"{name} muss ein Dictionary oder ein JSON-String sein.")
            return False

    _parse(base, 'base_json')
    _parse(target, 'target_json')
        
    return len(errors) == 0, errors
