def validate_request(data):
    if not isinstance(data, dict):
        return False, ["Daten müssen ein JSON-Objekt sein."]

    errors = []
    
    title = data.get('title')
    description = data.get('description')
    image_url = data.get('image_url')
    domain = data.get('domain')

    if title is not None and not isinstance(title, str):
        errors.append("'title' muss ein String sein.")
    if description is not None and not isinstance(description, str):
        errors.append("'description' muss ein String sein.")
    if image_url is not None and not isinstance(image_url, str):
        errors.append("'image_url' muss ein String sein.")
    if domain is not None and not isinstance(domain, str):
        errors.append("'domain' muss ein String sein.")

    # At least one field should be present
    if not any([title, description, image_url, domain]):
        errors.append("Mindestens ein Feld (title, description, image_url, domain) muss angegeben werden.")

    if errors:
        return False, errors
    return True, []
