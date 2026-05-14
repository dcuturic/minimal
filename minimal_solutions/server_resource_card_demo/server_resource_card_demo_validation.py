from app.validation import Validator

def validate_resource_request(data):
    rules = {
        "cpu": {
            "required": True,
        },
        "ram": {
            "required": True,
        },
        "disk": {
            "required": True,
        }
    }
    
    is_valid, errors = Validator.validate(data, rules)
    
    if is_valid:
        for field in ["cpu", "ram", "disk"]:
            val = data.get(field)
            if not isinstance(val, (int, float)):
                try:
                    val = float(val)
                except (ValueError, TypeError):
                    is_valid = False
                    errors[field] = ["Muss eine Zahl sein."]
                    continue
            
            val = float(val)
            if val < 0 or val > 100:
                is_valid = False
                errors[field] = ["Muss zwischen 0 und 100 liegen."]
                
    return is_valid, errors
