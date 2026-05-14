def validate_case_converter_request(data):
    errors = {}
    
    if not isinstance(data, dict):
        return False, {"_all": "Payload must be a JSON object."}
        
    text = data.get('text')
    if text is None or not isinstance(text, str):
        errors['text'] = "Feld 'text' ist erforderlich und muss ein String sein."
        
    target_case = data.get('target_case')
    valid_cases = ['uppercase', 'lowercase', 'titlecase', 'camelcase', 'snakecase', 'kebabcase', 'pascalcase']
    if target_case not in valid_cases:
        errors['target_case'] = f"Feld 'target_case' muss einer der folgenden Werte sein: {', '.join(valid_cases)}."
        
    return len(errors) == 0, errors
