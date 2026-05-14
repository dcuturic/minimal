def validate_openapi_request(data):
    if not isinstance(data, dict):
        return False, ["Erwartet wurde ein JSON-Objekt/Dictionary."]
    
    errors = []
    
    if 'path' not in data:
        errors.append("Feld 'path' fehlt.")
    elif not isinstance(data['path'], str):
        errors.append("Feld 'path' muss ein String sein.")
    elif not data['path'].startswith('/'):
        errors.append("Feld 'path' muss mit einem '/' beginnen.")

    if 'method' not in data:
        errors.append("Feld 'method' fehlt.")
    elif not isinstance(data['method'], str):
        errors.append("Feld 'method' muss ein String sein.")
    elif data['method'].upper() not in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']:
        errors.append("Feld 'method' muss GET, POST, PUT, PATCH oder DELETE sein.")

    if 'summary' not in data:
        errors.append("Feld 'summary' fehlt.")
    elif not isinstance(data['summary'], str):
        errors.append("Feld 'summary' muss ein String sein.")
    elif not data['summary'].strip():
        errors.append("Feld 'summary' darf nicht leer sein.")

    if 'request_fields' in data:
        if not isinstance(data['request_fields'], (list, str)):
            errors.append("Feld 'request_fields' muss eine Liste oder ein kommagetrennter String sein.")

    return len(errors) == 0, errors
