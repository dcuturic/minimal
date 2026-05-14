def validate_request(data):
    errors = []
    
    if not data:
        return False, [{"field": "body", "message": "Request body is empty or invalid JSON."}]
    
    topic = data.get('topic', '')
    if not isinstance(topic, str) or not topic.strip():
        errors.append({"field": "topic", "message": "Das Feld 'topic' darf nicht leer sein."})
        
    voice_style = data.get('voice_style', '')
    if not isinstance(voice_style, str) or not voice_style.strip():
        errors.append({"field": "voice_style", "message": "Das Feld 'voice_style' darf nicht leer sein."})
        
    duration = data.get('duration', '')
    if not isinstance(duration, str) or not duration.strip():
        errors.append({"field": "duration", "message": "Das Feld 'duration' darf nicht leer sein."})
        
    return len(errors) == 0, errors
