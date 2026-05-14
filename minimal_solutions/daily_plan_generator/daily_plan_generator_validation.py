def validate_daily_plan_request(data):
    errors = {}
    
    if not isinstance(data, dict):
        return False, {"request": "Erwartet wurde ein JSON-Objekt."}
        
    tasks = data.get("tasks")
    if tasks is None:
        errors["tasks"] = "Feld ist erforderlich."
    elif not isinstance(tasks, list):
        errors["tasks"] = "Muss eine Liste sein."
    elif len(tasks) == 0:
        errors["tasks"] = "Liste darf nicht leer sein."
    else:
        for item in tasks:
            if not isinstance(item, str):
                errors["tasks"] = "Alle Tasks müssen Strings sein."
                break
                
    available_hours = data.get("available_hours")
    if available_hours is None:
        errors["available_hours"] = "Feld ist erforderlich."
    else:
        try:
            hours = float(available_hours)
            if hours <= 0:
                errors["available_hours"] = "Wert muss > 0 sein."
        except (ValueError, TypeError):
            errors["available_hours"] = "Wert muss eine Zahl sein."
            
    if errors:
        return False, errors
        
    return True, {}
