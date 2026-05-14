from app.validation import Validator

def validate_request(data):
    rules = {
        "label": {"required": True, "type": str},
        "value": {"required": True, "type": str},
        "style": {"required": False, "type": str}
    }

    is_valid, errors = Validator.validate(data, rules)
    
    if is_valid:
        style = data.get('style', 'flat')
        valid_styles = ['flat', 'classic', 'plastic', 'for-the-badge', 'social']
        if style not in valid_styles:
            is_valid = False
            errors['style'] = [f"Der Style muss einer der folgenden sein: {', '.join(valid_styles)}."]
            
    return is_valid, errors
