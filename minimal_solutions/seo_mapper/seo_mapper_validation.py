from app.validation import Validator

def validate_seo_mapper_request(data: dict) -> tuple[bool, dict]:
    """
    Validiert die Eingabedaten für den SEO Mapper mittels globalem Validator.
    
    Erwartet:
      - topic: str (required)
      - target: str (required)
      - options: dict (optional)
      
    Returns:
        (is_valid: bool, errors: dict)
    """
    rules = {
        "topic": {
            "required": True,
            "type": str
        },
        "target": {
            "required": True,
            "type": str
        },
        "options": {
            "required": False,
            "type": str
        }
    }
    return Validator.validate(data, rules)
