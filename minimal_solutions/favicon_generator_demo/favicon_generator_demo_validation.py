from app.validation import Validator
import re

def validate_request(data):
    rules = {
        "letters": {"required": True, "type": str},
        "primary_color": {"required": True, "type": str},
        "shape": {"required": True, "type": str}
    }

    is_valid, errors = Validator.validate(data, rules)
    
    if is_valid:
        letters = data.get('letters', '')
        if len(letters) < 1 or len(letters) > 2:
            is_valid = False
            errors['letters'] = ["Es dürfen maximal 2 Buchstaben verwendet werden."]
            
        primary_color = data.get('primary_color', '')
        if not re.match(r'^#(?:[0-9a-fA-F]{3}){1,2}$', primary_color):
            is_valid = False
            errors['primary_color'] = ["Die Farbe muss ein gültiger Hex-Code sein (z.B. #ff0000)."]
            
        shape = data.get('shape', '')
        if shape not in ['square', 'circle', 'rounded']:
            is_valid = False
            errors['shape'] = ["Die Form muss 'square', 'circle' oder 'rounded' sein."]
            
    return is_valid, errors
