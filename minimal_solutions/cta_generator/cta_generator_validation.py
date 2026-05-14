def validate_cta_request(data):
    errors = {}
    if not data:
        return False, {"payload": "Missing JSON body"}
    
    topic = data.get('topic')
    audience = data.get('audience')
    tone = data.get('tone')
    
    if not topic or not str(topic).strip():
        errors['topic'] = 'Topic is required.'
        
    if not audience or not str(audience).strip():
        errors['audience'] = 'Audience is required.'
        
    if not tone or not str(tone).strip():
        errors['tone'] = 'Tone is required.'
        
    if errors:
        return False, errors
        
    return True, None
