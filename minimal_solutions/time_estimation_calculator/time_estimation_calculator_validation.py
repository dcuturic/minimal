def validate_time_estimation_request(data):
    errors = {}
    if not isinstance(data, dict):
        return False, {"request": "Input must be a JSON object"}
        
    fields = ['ticket_count', 'minutes_per_ticket', 'days', 'workers']
    for field in fields:
        if field not in data:
            errors[field] = "Feld ist erforderlich."
        else:
            try:
                val = float(data[field])
                if val < 0:
                    errors[field] = "Wert muss >= 0 sein."
            except (ValueError, TypeError):
                errors[field] = "Wert muss eine Zahl sein."
                
    return len(errors) == 0, errors
