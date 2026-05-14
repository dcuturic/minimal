def validate_component_json_builder_input(data):
    errors = {}
    if not isinstance(data, dict):
        return False, {"payload": "Invalid JSON format"}
    
    if not data.get("template"):
        errors["template"] = "Template is required."
    
    if errors:
        return False, errors
    return True, {}
