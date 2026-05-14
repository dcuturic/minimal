def validate_hosting_analyzer_request(data):
    errors = {}
    if not isinstance(data, dict):
        return False, {"payload": "Must be a dictionary"}
        
    source = data.get('source')
    if source is None:
        errors['source'] = "Field 'source' is required."
    elif not isinstance(source, str):
        errors['source'] = "Field 'source' must be a string."
    elif not source.strip():
        errors['source'] = "Field 'source' cannot be empty."

    config = data.get('config')
    if config is not None and not isinstance(config, (dict, str)):
        errors['config'] = "Field 'config' must be a dictionary or a JSON string."

    mode = data.get('mode')
    if mode is not None and not isinstance(mode, str):
        errors['mode'] = "Field 'mode' must be a string."

    if not errors:
        return True, None
    return False, errors
