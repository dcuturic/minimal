import re

def validate_health_check_request(data):
    if not isinstance(data, dict):
        return False, {"__root__": "Erwartet wurde ein JSON-Objekt/Dictionary."}

    errors = {}
    url = data.get('url')

    if not url:
        errors['url'] = "URL ist ein Pflichtfeld."
    elif not isinstance(url, str):
        errors['url'] = "URL muss ein String sein."
    else:
        # Basic URL validation
        pattern = re.compile(
            r'^https?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        if not pattern.match(url):
            errors['url'] = "Ungültige URL."

    if errors:
        return False, errors
    return True, {}
