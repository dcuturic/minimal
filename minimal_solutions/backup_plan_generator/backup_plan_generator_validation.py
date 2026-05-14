from app.validation import Validator

def validate_backup_plan_request(data):
    rules = {
        "frequency": {
            "required": True,
            "type": str,
        },
        "retention_days": {
            "required": True,
            "type": int,
        },
        "storage_type": {
            "required": True,
            "type": str,
        }
    }
    is_valid, errors = Validator.validate(data, rules)
    
    if is_valid:
        valid_frequencies = ["hourly", "daily", "weekly", "monthly"]
        if data.get("frequency") not in valid_frequencies:
            errors["frequency"] = ["Erwartet wurde einer der Werte: hourly, daily, weekly, monthly."]
            is_valid = False
            
        valid_storage = ["local", "s3", "azure", "gcs"]
        if data.get("storage_type") not in valid_storage:
            errors["storage_type"] = ["Erwartet wurde einer der Werte: local, s3, azure, gcs."]
            is_valid = False
            
        retention = data.get("retention_days")
        if not isinstance(retention, int) or retention <= 0:
            errors["retention_days"] = ["Die Aufbewahrungsdauer muss eine positive Zahl sein."]
            is_valid = False

    return is_valid, errors
