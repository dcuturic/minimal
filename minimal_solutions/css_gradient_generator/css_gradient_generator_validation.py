from app.validation import Validator

def validate_gradient_request(data):
    rules = {
        "colors": {"required": True, "type": list},
        "angle": {"required": True, "type": int},
        "type": {"required": True, "type": str}
    }

    is_valid, errors = Validator.validate(data, rules)
    
    if is_valid:
        colors = data.get('colors', [])
        if len(colors) < 2:
            is_valid = False
            errors['colors'] = ["Es müssen mindestens zwei Farben angegeben werden."]
        else:
            for c in colors:
                if not isinstance(c, str) or not c.strip():
                    is_valid = False
                    errors['colors'] = ["Alle Farben müssen gültige Zeichenketten sein."]
                    break

        angle = data.get('angle')
        if angle < 0 or angle > 360:
            is_valid = False
            errors['angle'] = ["Der Winkel muss zwischen 0 und 360 Grad liegen."]

        gradient_type = data.get('type')
        if gradient_type not in ['linear', 'radial']:
            is_valid = False
            errors['type'] = ["Der Typ muss entweder 'linear' oder 'radial' sein."]

    return is_valid, errors
