from typing import Tuple, Dict

def validate_landingpage_formatter_request(data: dict) -> Tuple[bool, Dict[str, str]]:
    errors = {}
    
    if not isinstance(data, dict):
        return False, {"request": "Invalid JSON format"}
        
    topic = data.get('topic')
    target = data.get('target')
    options = data.get('options')
    
    if topic is None:
        errors['topic'] = "Das Feld 'topic' ist erforderlich."
    elif not isinstance(topic, str):
        errors['topic'] = "Das Feld 'topic' muss ein String sein."
    elif len(topic.strip()) == 0:
        errors['topic'] = "Das Feld 'topic' darf nicht leer sein."
        
    if target is None:
        errors['target'] = "Das Feld 'target' ist erforderlich."
    elif not isinstance(target, str):
        errors['target'] = "Das Feld 'target' muss ein String sein."
    elif len(target.strip()) == 0:
        errors['target'] = "Das Feld 'target' darf nicht leer sein."

    if options is not None and not isinstance(options, str):
        errors['options'] = "Das Feld 'options' muss ein String sein."
        
    return len(errors) == 0, errors
