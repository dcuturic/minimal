def validate_seo_formatter_input(data):
    errors = {}
    if not data:
        return False, {"general": "Request body must be JSON."}
    
    if not data.get('topic') or not isinstance(data.get('topic'), str) or not data['topic'].strip():
        errors['topic'] = "Topic ist erforderlich und muss ein String sein."
    
    if not data.get('target') or not isinstance(data.get('target'), str) or not data['target'].strip():
        errors['target'] = "Target ist erforderlich und muss ein String sein."
        
    options = data.get('options', {})
    if not isinstance(options, dict):
        errors['options'] = "Options muss ein Dictionary sein."

    if errors:
        return False, errors
    return True, None
