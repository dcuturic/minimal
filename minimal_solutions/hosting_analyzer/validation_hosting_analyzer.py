def validate_hosting_analyzer_request(data):
    errors = {}
    if not isinstance(data, dict):
        return False, {"payload": "Must be a dictionary"}
        
    if not errors:
        return True, None
    return False, errors
