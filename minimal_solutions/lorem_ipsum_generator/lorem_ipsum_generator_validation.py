from typing import Dict, Any, Tuple

ALLOWED_MODES = ['paragraphs', 'words', 'bytes', 'lists']

def validate_lorem_ipsum_generator_request(data: Dict[str, Any]) -> Tuple[bool, Dict[str, str]]:
    errors = {}
    
    if 'mode' not in data:
        errors['mode'] = "mode ist erforderlich."
    elif not isinstance(data['mode'], str):
        errors['mode'] = "mode muss ein String sein."
    elif data['mode'] not in ALLOWED_MODES:
        errors['mode'] = f"mode muss einer der folgenden Werte sein: {', '.join(ALLOWED_MODES)}."
        
    if 'count' not in data:
        errors['count'] = "count ist erforderlich."
    elif not isinstance(data['count'], int) or data['count'] < 1 or data['count'] > 100000:
        errors['count'] = "count muss eine Ganzzahl zwischen 1 und 100000 sein."
        
    return len(errors) == 0, errors
