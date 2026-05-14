def validate_summarizer_request(data):
    errors = {}
    if not data or not isinstance(data, dict):
        return False, {"general": "Keine Daten empfangen oder ungültiges Format."}
    
    if 'topic' not in data or not str(data['topic']).strip():
        errors['topic'] = "Topic is required"
        
    if 'target' not in data or not str(data['target']).strip():
        errors['target'] = "Target is required"
        
    options = data.get('options')
    if options is not None and not isinstance(options, (dict, str)):
        errors['options'] = "Options must be a dictionary or string"
        
    if errors:
        return False, errors
        
    return True, {}
