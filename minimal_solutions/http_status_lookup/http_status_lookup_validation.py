def validate_http_status_request(data):
    if not isinstance(data, dict):
        return False, {"payload": "Invalid JSON format."}
    
    status_code = data.get("status_code")
    if status_code is None:
        return False, {"status_code": "Fehlt."}
    
    try:
        status_code = int(status_code)
    except (ValueError, TypeError):
        return False, {"status_code": "Muss eine Zahl sein."}
        
    if not (100 <= status_code <= 599):
        return False, {"status_code": "Status Code muss zwischen 100 und 599 liegen."}
        
    return True, {}
