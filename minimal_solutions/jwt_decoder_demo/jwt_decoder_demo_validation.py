def validate_jwt_request(data):
    errors = {}
    if not isinstance(data, dict):
        return False, {"_all": "Erwartet wurde ein JSON-Objekt/Dictionary."}
    
    jwt_token = data.get("jwt")
    if jwt_token is None:
        errors["jwt"] = "Feld 'jwt' fehlt."
    elif not isinstance(jwt_token, str):
        errors["jwt"] = "Feld 'jwt' muss ein String sein."
    elif not jwt_token.strip():
        errors["jwt"] = "Feld 'jwt' darf nicht leer sein."
    else:
        parts = jwt_token.split('.')
        if len(parts) != 3:
            errors["jwt"] = "Ungültiges JWT-Format. Ein JWT muss aus drei Teilen bestehen (getrennt durch Punkte)."

    if errors:
        return False, errors
    return True, {}
