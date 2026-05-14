def validate_hash_generator_request(data):
    errors = {}
    if not isinstance(data, dict):
        return False, {"payload": "Erwartet wurde ein JSON-Objekt."}
        
    if "text" not in data:
        errors["text"] = "Das Feld 'text' fehlt."
    elif not isinstance(data["text"], str):
        errors["text"] = "Das Feld 'text' muss ein String sein."
        
    if "algorithm" not in data:
        errors["algorithm"] = "Das Feld 'algorithm' fehlt."
    elif data["algorithm"] not in ['md5', 'sha1', 'sha256', 'sha512']:
        errors["algorithm"] = "Ungültiger Algorithmus."
        
    if errors:
        return False, errors
    return True, {}
