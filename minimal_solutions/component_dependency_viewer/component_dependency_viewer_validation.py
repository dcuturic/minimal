def validate_component_dependency_viewer_input(data):
    if not isinstance(data, dict):
        return False, {"data": "Eingabe muss ein JSON-Objekt sein."}
    
    errors = {}
    if 'component_json' not in data:
        errors['component_json'] = 'Das Feld component_json ist erforderlich.'
    else:
        component_json = data['component_json']
        if not isinstance(component_json, (str, dict)):
            errors['component_json'] = 'Das Feld component_json muss ein String oder ein Objekt sein.'

    return len(errors) == 0, errors
