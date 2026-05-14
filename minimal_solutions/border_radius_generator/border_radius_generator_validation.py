from app.validation import Validator

def validate_border_radius_request(data):
    rules = {
        "top_left": {"required": True, "type": (int, float), "type_name": "Zahl"},
        "top_right": {"required": True, "type": (int, float), "type_name": "Zahl"},
        "bottom_right": {"required": True, "type": (int, float), "type_name": "Zahl"},
        "bottom_left": {"required": True, "type": (int, float), "type_name": "Zahl"}
    }

    is_valid, errors = Validator.validate(data, rules)
    
    if is_valid:
        for field in ["top_left", "top_right", "bottom_right", "bottom_left"]:
            val = data.get(field)
            if val < 0:
                is_valid = False
                errors[field] = [f"Der Wert für {field} darf nicht negativ sein."]
            
    return is_valid, errors
