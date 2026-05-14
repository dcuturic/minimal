from app.validation import Validator
import re

def validate_request(data):
    rules = {
        "shape": {"required": True, "type": str},
        "color": {"required": True, "type": str},
        "label": {"required": False, "type": str}
    }

    is_valid, errors = Validator.validate(data, rules)
    
    if is_valid:
        shape = data.get('shape', '')
        valid_shapes = ['circle', 'square', 'rounded', 'star', 'hexagon', 'triangle', 'diamond', 'shield']
        if shape not in valid_shapes:
            is_valid = False
            errors['shape'] = [f"Die Form muss eine der folgenden sein: {', '.join(valid_shapes)}."]
            
        color = data.get('color', '')
        if not re.match(r'^#(?:[0-9a-fA-F]{3}){1,2}$', color):
            is_valid = False
            errors['color'] = ["Die Farbe muss ein gültiger Hex-Code sein (z.B. #ff0000)."]
            
        label = data.get('label', '')
        if label and len(label) > 2:
            is_valid = False
            errors['label'] = ["Das Label darf maximal 2 Zeichen lang sein."]
            
    return is_valid, errors
