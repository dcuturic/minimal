def validate_diff_viewer_request(data):
    if not isinstance(data, dict):
        return False, {"payload": "Invalid JSON format"}
    
    errors = {}
    
    topic = data.get('topic')
    if not topic or not isinstance(topic, str):
        errors['topic'] = "Topic is required and must be a string."
    elif len(topic) < 3:
        errors['topic'] = "Topic must be at least 3 characters long."
        
    target = data.get('target')
    if not target or not isinstance(target, str):
        errors['target'] = "Target is required and must be a string."
    elif len(target) < 3:
        errors['target'] = "Target must be at least 3 characters long."
        
    options = data.get('options')
    if options is not None and not isinstance(options, str):
        errors['options'] = "Options must be a string if provided."
        
    if errors:
        return False, errors
        
    return True, None
