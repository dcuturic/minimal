def validate_hosting_template_builder_request(data):
    """
    Validiert die Anfrage für den Hosting Template Builder.
    Erwartet ein Dictionary mit den Schlüsseln 'source', 'config' und 'mode'.
    """
    errors = {}

    if not isinstance(data, dict):
        return False, {"payload": "Erwartet wurde ein JSON-Objekt/Dictionary."}

    # Validate 'source'
    if "source" not in data:
        errors["source"] = "Feld 'source' fehlt."
    elif not isinstance(data["source"], str) or not data["source"].strip():
        errors["source"] = "Feld 'source' muss ein nicht-leerer String sein."

    # Validate 'config'
    if "config" in data and not isinstance(data["config"], dict):
        errors["config"] = "Feld 'config' muss ein Objekt/Dictionary sein."

    # Validate 'mode'
    if "mode" not in data:
        errors["mode"] = "Feld 'mode' fehlt."
    elif not isinstance(data["mode"], str) or not data["mode"].strip():
        errors["mode"] = "Feld 'mode' muss ein nicht-leerer String sein."

    if errors:
        return False, errors

    return True, {}
