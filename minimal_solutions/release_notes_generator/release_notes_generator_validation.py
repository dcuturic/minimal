from typing import Tuple, Dict

def validate_release_notes_request(data: dict) -> Tuple[bool, Dict[str, str]]:
    errors = {}
    
    if not isinstance(data, dict):
        return False, {"request": "Invalid JSON format"}
        
    version = data.get('version')
    features = data.get('features')
    fixes = data.get('fixes')
    breaking_changes = data.get('breaking_changes')
    
    if not version:
        errors['version'] = "Das Feld 'version' ist erforderlich."
    elif not isinstance(version, str):
        errors['version'] = "Das Feld 'version' muss ein String sein."
    elif len(version.strip()) == 0:
        errors['version'] = "Das Feld 'version' darf nicht leer sein."

    if features is not None:
        if not isinstance(features, list):
            errors['features'] = "Das Feld 'features' muss eine Liste sein."
        else:
            for item in features:
                if not isinstance(item, str):
                    errors['features'] = "Alle Elemente in 'features' müssen Strings sein."
                    break

    if fixes is not None:
        if not isinstance(fixes, list):
            errors['fixes'] = "Das Feld 'fixes' muss eine Liste sein."
        else:
            for item in fixes:
                if not isinstance(item, str):
                    errors['fixes'] = "Alle Elemente in 'fixes' müssen Strings sein."
                    break

    if breaking_changes is not None:
        if not isinstance(breaking_changes, list):
            errors['breaking_changes'] = "Das Feld 'breaking_changes' muss eine Liste sein."
        else:
            for item in breaking_changes:
                if not isinstance(item, str):
                    errors['breaking_changes'] = "Alle Elemente in 'breaking_changes' müssen Strings sein."
                    break
        
    return len(errors) == 0, errors
