def validate_word_replacer_request(data):
    errors = {}
    
    if not isinstance(data, dict):
        return False, {"request": "Payload muss ein JSON-Objekt sein."}
        
    text = data.get("text")
    if text is None:
        errors["text"] = "Text ist ein Pflichtfeld."
    elif not isinstance(text, str):
        errors["text"] = "Text muss ein String sein."
        
    search = data.get("search")
    if search is None:
        errors["search"] = "Search ist ein Pflichtfeld."
    elif not isinstance(search, str):
        errors["search"] = "Search muss ein String sein."
    elif len(search) == 0:
        errors["search"] = "Search darf nicht leer sein."
        
    replace = data.get("replace")
    if replace is None:
        errors["replace"] = "Replace ist ein Pflichtfeld."
    elif not isinstance(replace, str):
        errors["replace"] = "Replace muss ein String sein."
        
    case_sensitive = data.get("case_sensitive", False)
    if case_sensitive not in [True, False, "true", "false", "True", "False"]:
        errors["case_sensitive"] = "Case Sensitive muss ein Boolean sein."

    return len(errors) == 0, errors
