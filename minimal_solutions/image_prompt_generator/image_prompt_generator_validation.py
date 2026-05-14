def validate_request(data):
    errors = []
    
    if not data:
        return False, [{"field": "body", "message": "Request body is empty or invalid JSON."}]
    
    subject = data.get('subject', '')
    if not isinstance(subject, str) or not subject.strip():
        errors.append({"field": "subject", "message": "Das Feld 'subject' darf nicht leer sein."})
        
    style = data.get('style', '')
    if not isinstance(style, str) or not style.strip():
        errors.append({"field": "style", "message": "Das Feld 'style' darf nicht leer sein."})
        
    mood = data.get('mood', '')
    if not isinstance(mood, str) or not mood.strip():
        errors.append({"field": "mood", "message": "Das Feld 'mood' darf nicht leer sein."})
        
    aspect_ratio = data.get('aspect_ratio', '')
    if not isinstance(aspect_ratio, str) or not aspect_ratio.strip():
        errors.append({"field": "aspect_ratio", "message": "Das Feld 'aspect_ratio' darf nicht leer sein."})
        
    return len(errors) == 0, errors
