def validate_request(data):
    errors = {}
    if not isinstance(data, dict):
        return False, {"payload": ["Invalid payload format."]}
    
    topic = data.get("topic")
    target = data.get("target")

    if not topic or not isinstance(topic, str):
        errors["topic"] = ["Topic is required and must be a string."]
    elif len(topic.strip()) < 3:
        errors["topic"] = ["Topic must be at least 3 characters long."]

    if not target or not isinstance(target, str):
        errors["target"] = ["Target is required and must be a string."]
    elif len(target.strip()) < 3:
        errors["target"] = ["Target must be at least 3 characters long."]
        
    if errors:
        return False, errors
    return True, None
