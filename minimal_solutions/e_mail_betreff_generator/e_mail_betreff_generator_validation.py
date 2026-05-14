def validate_e_mail_betreff_generator_input(data):
    if not isinstance(data, dict):
        return False, {"data": "Input must be a JSON object."}
    
    errors = {}
    
    topic = data.get('topic')
    if not topic or not isinstance(topic, str) or not topic.strip():
        errors['topic'] = "Topic is required and must be a non-empty string."
        
    audience = data.get('audience')
    if not audience or not isinstance(audience, str) or not audience.strip():
        errors['audience'] = "Audience is required and must be a non-empty string."
        
    tone = data.get('tone')
    if not tone or not isinstance(tone, str) or not tone.strip():
        errors['tone'] = "Tone is required and must be a non-empty string."
        
    if errors:
        return False, errors
    return True, {}
