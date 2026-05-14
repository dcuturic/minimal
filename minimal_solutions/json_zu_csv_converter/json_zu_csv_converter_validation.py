def validate_json_zu_csv_converter_request(data):
    errors = {}
    if not isinstance(data, dict):
        return False, {"payload": "Erwartet wurde ein JSON-Objekt."}
        
    if "json_text" not in data:
        errors["json_text"] = "Das Feld 'json_text' fehlt."
    elif not isinstance(data["json_text"], str):
        errors["json_text"] = "Das Feld 'json_text' muss ein String sein."
    elif not data["json_text"].strip():
        errors["json_text"] = "Das Feld 'json_text' darf nicht leer sein."
        
    if "delimiter" in data:
        if not isinstance(data["delimiter"], str):
            errors["delimiter"] = "Das Feld 'delimiter' muss ein String sein."
        elif len(data["delimiter"]) != 1:
            errors["delimiter"] = "Das Feld 'delimiter' muss genau ein Zeichen lang sein."
            
    if errors:
        return False, errors
    return True, {}
