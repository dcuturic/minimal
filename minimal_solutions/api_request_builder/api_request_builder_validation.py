from typing import Tuple, Dict

def validate_api_request(data: dict) -> Tuple[bool, Dict[str, str]]:
    errors = {}
    
    if not isinstance(data, dict):
        return False, {"request": "Invalid JSON format"}
        
    method = data.get('method')
    url = data.get('url')
    headers = data.get('headers')
    
    if not method:
        errors['method'] = "Das Feld 'method' ist erforderlich."
    elif not isinstance(method, str):
        errors['method'] = "Das Feld 'method' muss ein String sein."
    elif method.upper() not in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS', 'HEAD']:
        errors['method'] = "Ungültige HTTP-Methode."
        
    if not url:
        errors['url'] = "Das Feld 'url' ist erforderlich."
    elif not isinstance(url, str):
        errors['url'] = "Das Feld 'url' muss ein String sein."
    elif not (url.startswith('http://') or url.startswith('https://')):
        errors['url'] = "Die URL muss mit http:// oder https:// beginnen."
        
    if headers is not None and not isinstance(headers, dict):
        errors['headers'] = "Das Feld 'headers' muss ein JSON-Objekt (Dictionary) sein."
        
    return len(errors) == 0, errors
