def validate_curl_request(data):
    if not isinstance(data, dict):
        return False, ["Erwartet wurde ein JSON-Objekt/Dictionary."]
    
    errors = []
    
    if 'method' not in data:
        errors.append("Feld 'method' fehlt.")
    elif not isinstance(data['method'], str):
        errors.append("Feld 'method' muss ein String sein.")
    elif data['method'].upper() not in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']:
        errors.append("Feld 'method' muss GET, POST, PUT, PATCH oder DELETE sein.")

    if 'url' not in data:
        errors.append("Feld 'url' fehlt.")
    elif not isinstance(data['url'], str):
        errors.append("Feld 'url' muss ein String sein.")
    elif not data['url'].strip():
        errors.append("Feld 'url' darf nicht leer sein.")

    if 'headers' in data:
        if not isinstance(data['headers'], dict):
            errors.append("Feld 'headers' muss ein Objekt/Dictionary sein.")

    if 'body' in data:
        if not isinstance(data['body'], (dict, list, str, type(None))):
            errors.append("Feld 'body' muss ein Objekt, Array, String oder null sein.")

    return len(errors) == 0, errors
