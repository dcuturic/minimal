def validate_task_breakdown_request(data):
    errors = {}
    
    if not isinstance(data, dict):
        return False, {"request": "Erwartet wurde ein JSON-Objekt."}
        
    task_text = data.get("task_text")
    if not task_text or not isinstance(task_text, str):
        errors["task_text"] = "Task text is required and must be a string."
    elif len(task_text.strip()) == 0:
        errors["task_text"] = "Task text cannot be empty."
        
    depth = data.get("depth")
    if depth is not None:
        try:
            depth = int(depth)
            if depth not in [1, 2, 3]:
                errors["depth"] = "Depth must be 1, 2, or 3."
        except (ValueError, TypeError):
            errors["depth"] = "Depth must be an integer (1, 2, or 3)."
            
    if errors:
        return False, errors
        
    return True, {}
