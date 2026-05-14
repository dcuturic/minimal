from app.validation import Validator

def validate_minecraft_motd_preview_request(data):
    rules = {
        "motd_text": {
            "required": True,
            "type": str,
            "type_name": "String"
        }
    }
    return Validator.validate(data, rules)
