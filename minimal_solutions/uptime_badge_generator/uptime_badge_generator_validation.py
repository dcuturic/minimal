from app.validation import Validator

def validate_badge_request(data):
    rules = {
        "status": {
            "required": True,
            "type": str,
            "min_length": 1,
            "max_length": 50
        },
        "uptime_percent": {
            "required": True,
        }
    }
    
    is_valid, errors = Validator.validate(data, rules)
    
    if is_valid:
        uptime = data.get("uptime_percent")
        if not isinstance(uptime, (int, float)):
            try:
                float(uptime)
            except ValueError:
                is_valid = False
                errors["uptime_percent"] = ["Muss eine Zahl sein."]
        
        if is_valid:
            val = float(uptime)
            if val < 0 or val > 100:
                is_valid = False
                errors["uptime_percent"] = ["Muss zwischen 0 und 100 liegen."]
            
    return is_valid, errors
