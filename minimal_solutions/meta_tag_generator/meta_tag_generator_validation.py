def validate_meta_tag_request(data):
    if not isinstance(data, dict):
        return False, ["Erwartet wurde ein JSON-Objekt/Dictionary."]
    
    errors = []
    
    title = data.get('title')
    description = data.get('description')
    image_url = data.get('image_url')
    page_url = data.get('page_url')
    
    if title is not None and not isinstance(title, str):
        errors.append("'title' muss ein String sein.")
    if description is not None and not isinstance(description, str):
        errors.append("'description' muss ein String sein.")
    if image_url is not None and not isinstance(image_url, str):
        errors.append("'image_url' muss ein String sein.")
    if page_url is not None and not isinstance(page_url, str):
        errors.append("'page_url' muss ein String sein.")
        
    if not title and not description:
        errors.append("Mindestens 'title' oder 'description' muss angegeben werden.")
        
    if errors:
        return False, errors
        
    return True, []
