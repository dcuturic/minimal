from typing import Tuple, Dict, Any

def validate_preview_card_request(data: Any) -> Tuple[bool, Dict[str, str]]:
    if not isinstance(data, dict):
        return False, {"_error": "Payload must be a JSON object."}
        
    errors = {}
    
    component_name = data.get('component_name')
    if not component_name or not isinstance(component_name, str):
        errors['component_name'] = "component_name ist erforderlich und muss ein String sein."
        
    category = data.get('category')
    if not category or not isinstance(category, str):
        errors['category'] = "category ist erforderlich und muss ein String sein."
        
    preview_html = data.get('preview_html')
    if preview_html is None or not isinstance(preview_html, str):
        errors['preview_html'] = "preview_html ist erforderlich und muss ein String sein."
        
    if errors:
        return False, errors
        
    return True, {}
