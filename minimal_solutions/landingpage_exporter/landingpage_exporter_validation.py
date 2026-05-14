def validate_exporter_request(data):
    if not isinstance(data, dict):
        return False, ["Erwartet wurde ein JSON-Objekt/Dictionary."]

    errors = {}
    
    topic = data.get('topic')
    target = data.get('target')
    options = data.get('options')
    
    if not topic or not isinstance(topic, str) or not topic.strip():
        errors['topic'] = "Das Feld 'topic' ist erforderlich und darf nicht leer sein."
        
    if not target or not isinstance(target, str) or not target.strip():
        errors['target'] = "Das Feld 'target' ist erforderlich und darf nicht leer sein."
        
    if options is not None and not isinstance(options, str):
        errors['options'] = "Das Feld 'options' muss ein String sein."

    if len(errors) > 0:
        return False, errors
        
    return True, {}
