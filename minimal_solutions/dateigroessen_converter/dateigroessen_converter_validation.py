from app.validation import Validator

def validate_request(data):
    rules = {
        "value": {
            "required": True,
            "type": (int, float),
            "type_name": "Zahl"
        },
        "from_unit": {
            "required": True,
            "type": str
        },
        "to_unit": {
            "required": True,
            "type": str
        }
    }
    
    is_valid, errors = Validator.validate(data, rules)
    if not is_valid:
        return False, errors

    valid_units = ["B", "KB", "MB", "GB", "TB"]
    if data["from_unit"] not in valid_units:
        errors["from_unit"] = [f"Ungültige Einheit. Erlaubt sind: {', '.join(valid_units)}"]
    
    if data["to_unit"] not in valid_units:
        errors["to_unit"] = [f"Ungültige Einheit. Erlaubt sind: {', '.join(valid_units)}"]
        
    if errors:
        return False, errors
        
    return True, None
