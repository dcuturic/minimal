def validate_importer_request(data):
    if not isinstance(data, dict):
        return False, ["Erwartet wurde ein JSON-Objekt/Dictionary."]

    errors = []
    
    topic = data.get('topic')
    target = data.get('target')
    
    if not topic or not isinstance(topic, str) or not topic.strip():
        errors.append("Das Feld 'topic' ist erforderlich und darf nicht leer sein.")
        
    if not target or not isinstance(target, str) or not target.strip():
        errors.append("Das Feld 'target' ist erforderlich und darf nicht leer sein.")
        
    if len(errors) > 0:
        return False, errors
        
    return True, []
