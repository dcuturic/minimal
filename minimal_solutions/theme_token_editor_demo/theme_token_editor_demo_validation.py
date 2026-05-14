def validate_theme_token_editor_request(data):
    errors = []
    
    if not isinstance(data, dict):
        return False, [{"field": "body", "message": "Request body must be a JSON object"}]
        
    if "tokens" not in data:
        errors.append({"field": "tokens", "message": "Field 'tokens' is required"})
    elif not isinstance(data["tokens"], dict):
        errors.append({"field": "tokens", "message": "Field 'tokens' must be an object"})
        
    return len(errors) == 0, errors
