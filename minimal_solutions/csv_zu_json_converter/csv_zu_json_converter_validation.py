def validate_input(data):
    errors = {}
    if not data:
        return False, {"payload": "Invalid JSON payload"}
    
    if 'csv_text' not in data or not isinstance(data['csv_text'], str) or not data['csv_text'].strip():
        errors['csv_text'] = "CSV-Text ist erforderlich."
        
    if 'delimiter' in data:
        delimiter = data['delimiter']
        if not isinstance(delimiter, str) or len(delimiter) != 1:
            errors['delimiter'] = "Trennzeichen muss ein einzelnes Zeichen sein."
            
    if 'has_header' in data:
        has_header = data['has_header']
        if not isinstance(has_header, bool):
            # sometimes boolean comes as string from form data? The requirement says it accepts JSON.
            # allow boolean
            if has_header not in [True, False, 'true', 'false', 'True', 'False']:
                errors['has_header'] = "has_header muss ein Boolean sein."
        
    if errors:
        return False, errors
    return True, None
