def validate_lesezeit_rechner_request(data):
    errors = {}
    
    if not isinstance(data, dict):
        return False, {"request": "Payload muss ein JSON-Objekt sein."}
        
    text = data.get("text")
    if text is None:
        errors["text"] = "Text ist ein Pflichtfeld."
    elif not isinstance(text, str):
        errors["text"] = "Text muss ein String sein."
        
    words_per_minute = data.get("words_per_minute", 200)
    
    if isinstance(words_per_minute, str):
        try:
            words_per_minute = int(words_per_minute)
        except ValueError:
            errors["words_per_minute"] = "Wörter pro Minute muss eine gültige Zahl sein."
            
    if "words_per_minute" not in errors:
        if not isinstance(words_per_minute, (int, float)):
            errors["words_per_minute"] = "Wörter pro Minute muss eine Zahl sein."
        elif words_per_minute <= 0:
            errors["words_per_minute"] = "Wörter pro Minute muss größer als 0 sein."

    return len(errors) == 0, errors
