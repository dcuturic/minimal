from app.validation import Validator

def validate_box_shadow_request(data):
    rules = {
        "x": {"required": True, "type": (int, float), "type_name": "Zahl"},
        "y": {"required": True, "type": (int, float), "type_name": "Zahl"},
        "blur": {"required": True, "type": (int, float), "type_name": "Zahl"},
        "spread": {"required": True, "type": (int, float), "type_name": "Zahl"},
        "opacity": {"required": True, "type": (int, float), "type_name": "Zahl"},
        "color": {"required": False, "type": str, "type_name": "String"},
        "inset": {"required": False, "type": bool, "type_name": "Boolean"}
    }

    is_valid, errors = Validator.validate(data, rules)
    
    if is_valid:
        blur = data.get('blur')
        if blur < 0:
            is_valid = False
            errors['blur'] = ["Der Blur-Radius darf nicht negativ sein."]
            
        opacity = data.get('opacity')
        if opacity < 0 or opacity > 1:
            is_valid = False
            errors['opacity'] = ["Die Opacity muss zwischen 0 und 1 liegen."]
            
    return is_valid, errors
