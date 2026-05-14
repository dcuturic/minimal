from typing import Dict, Any, Tuple

ALLOWED_CATEGORIES = ['project', 'server', 'bot', 'fantasy', 'scifi', 'nature']

def validate_random_name_generator_request(data: Dict[str, Any]) -> Tuple[bool, Dict[str, str]]:
    errors = {}
    
    if 'category' not in data:
        errors['category'] = "category ist erforderlich."
    elif not isinstance(data['category'], str):
        errors['category'] = "category muss ein String sein."
    elif data['category'] not in ALLOWED_CATEGORIES:
        errors['category'] = f"category muss einer der folgenden Werte sein: {', '.join(ALLOWED_CATEGORIES)}."
        
    if 'count' not in data:
        errors['count'] = "count ist erforderlich."
    elif not isinstance(data['count'], int) or data['count'] < 1 or data['count'] > 100:
        errors['count'] = "count muss eine Ganzzahl zwischen 1 und 100 sein."
        
    return len(errors) == 0, errors
