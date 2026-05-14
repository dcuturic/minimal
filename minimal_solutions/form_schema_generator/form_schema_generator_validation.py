def validate_form_schema_request(data):
    if not isinstance(data, dict):
        return False, ["Payload must be a JSON object."]
    
    if 'fields' not in data:
        return False, ["Missing required field: 'fields'."]
    
    fields = data.get('fields')
    if not isinstance(fields, list):
        return False, ["'fields' must be a list."]
        
    errors = []
    for i, field in enumerate(fields):
        if not isinstance(field, dict):
            errors.append(f"Field at index {i} must be an object.")
            continue
            
        if 'name' not in field:
            errors.append(f"Field at index {i} is missing 'name'.")
        elif not isinstance(field['name'], str) or not field['name'].strip():
            errors.append(f"Field at index {i} must have a non-empty string 'name'.")
            
        if 'type' not in field:
            errors.append(f"Field at index {i} is missing 'type'.")
        elif not isinstance(field['type'], str) or not field['type'].strip():
            errors.append(f"Field at index {i} must have a non-empty string 'type'.")
            
    if errors:
        return False, errors
        
    return True, []
