def validate_headline_request(data):
    errors = {}
    
    if not isinstance(data, dict):
        return False, {"_error": "Erwartet wurde ein JSON-Objekt/Dictionary."}

    topic = data.get('topic')
    if not topic or not isinstance(topic, str) or len(topic.strip()) < 2:
        errors['topic'] = 'Topic ist erforderlich und muss mindestens 2 Zeichen lang sein.'

    style = data.get('style')
    if not style or not isinstance(style, str) or len(style.strip()) < 2:
        errors['style'] = 'Style ist erforderlich.'

    count = data.get('count')
    if count is not None:
        try:
            count = int(count)
            if count < 1 or count > 20:
                errors['count'] = 'Count muss zwischen 1 und 20 liegen.'
        except (ValueError, TypeError):
            errors['count'] = 'Count muss eine Zahl sein.'

    if errors:
        return False, errors
    return True, None
