def validate_kanban_ticket_request(data):
    errors = {}
    
    if not isinstance(data, dict):
        return False, {"request": "Erwartet wurde ein JSON-Objekt."}
        
    title = data.get("title")
    if not title or not isinstance(title, str):
        errors["title"] = "Title is required and must be a string."
    elif len(title.strip()) == 0:
        errors["title"] = "Title cannot be empty."
        
    priority = data.get("priority")
    if priority and priority not in ["low", "medium", "high"]:
        errors["priority"] = "Priority must be one of: low, medium, high."
        
    status = data.get("status")
    if status and status not in ["todo", "in_progress", "review", "done"]:
        errors["status"] = "Status must be one of: todo, in_progress, review, done."
        
    if errors:
        return False, errors
        
    return True, {}
