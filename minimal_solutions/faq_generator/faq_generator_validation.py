def validate_faq_generator_request(data):
    if not isinstance(data, dict):
        return False, ["Invalid data format. Expected JSON object."]
    
    errors = []
    source_text = data.get('source_text')
    count = data.get('count')
    
    if not source_text or not isinstance(source_text, str) or not source_text.strip():
        errors.append("Das Feld 'source_text' ist erforderlich und muss ein Text sein.")
        
    if count is not None:
        try:
            count = int(count)
            if count <= 0:
                errors.append("Die Anzahl 'count' muss eine positive Zahl sein.")
        except ValueError:
            errors.append("Die Anzahl 'count' muss eine ganze Zahl sein.")
            
    if errors:
        return False, errors
    return True, []
