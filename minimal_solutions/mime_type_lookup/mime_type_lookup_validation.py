def validate_mime_type_request(data):
    if not isinstance(data, dict):
        return False, {"payload": "Invalid JSON format."}
    
    query = data.get("query")
    if query is None:
        return False, {"query": "Fehlt."}
    
    if not isinstance(query, str) or not query.strip():
        return False, {"query": "Muss ein nicht-leerer String sein."}
        
    return True, {}
