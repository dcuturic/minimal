def validate_hosting_importer_request(data):
    errors = {}
    if "source" not in data or not str(data["source"]).strip():
        errors["source"] = "Source ist erforderlich"
    if "mode" not in data or not str(data["mode"]).strip():
        errors["mode"] = "Mode ist erforderlich"
    
    if errors:
        return False, errors
    return True, None
