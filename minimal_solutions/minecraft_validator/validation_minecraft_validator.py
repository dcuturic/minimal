def validate_minecraft_validator_request(data):
    """
    Validiert die Anfrage für den Minecraft Validator.
    Erwartet ein Dictionary mit den Schlüsseln 'input_text', 'mode' und optional 'options'.
    """
    errors = {}

    if not isinstance(data, dict):
        return False, {"payload": "Erwartet wurde ein JSON-Objekt/Dictionary."}

    # Validate 'input_text'
    if "input_text" not in data:
        errors["input_text"] = "Feld 'input_text' fehlt."
    elif not isinstance(data["input_text"], str) or not data["input_text"].strip():
        errors["input_text"] = "Feld 'input_text' muss ein nicht-leerer String sein."

    # Validate 'mode'
    if "mode" not in data:
        errors["mode"] = "Feld 'mode' fehlt."
    elif not isinstance(data["mode"], str) or not data["mode"].strip():
        errors["mode"] = "Feld 'mode' muss ein nicht-leerer String sein."

    # Validate 'options'
    if "options" in data and not isinstance(data["options"], dict):
        errors["options"] = "Feld 'options' muss ein Objekt/Dictionary sein."

    if errors:
        return False, errors

    return True, {}
