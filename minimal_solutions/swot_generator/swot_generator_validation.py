def validate_swot_generator_input(data):
    errors = {}
    
    if not isinstance(data, dict):
        return False, {"_root": "Eingabe muss ein Objekt sein."}
        
    topic = data.get('topic')
    if not topic:
        errors['topic'] = "Topic ist ein Pflichtfeld."
    elif not isinstance(topic, str):
        errors['topic'] = "Topic muss ein Text sein."
    elif len(topic.strip()) < 2:
        errors['topic'] = "Topic muss mindestens 2 Zeichen lang sein."
        
    notes = data.get('notes')
    if notes is not None:
        if not isinstance(notes, str):
            errors['notes'] = "Notes muss ein Text sein."
            
    return len(errors) == 0, errors
