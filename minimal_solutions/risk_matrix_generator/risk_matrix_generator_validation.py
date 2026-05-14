from app.validation import Validator

def validate_risk_matrix_request(data):
    rules = {
        "risks": {
            "required": True
        }
    }
    
    is_valid, errors = Validator.validate(data, rules)
    
    if is_valid:
        risks = data.get("risks")
        if not isinstance(risks, (list, str)):
            return False, {"risks": ["Das Feld 'risks' muss eine Liste oder ein String sein."]}
            
        if isinstance(risks, list):
            if len(risks) == 0:
                return False, {"risks": ["Die Liste der Risiken darf nicht leer sein."]}
        elif isinstance(risks, str):
            if not risks.strip():
                return False, {"risks": ["Der Text für Risiken darf nicht leer sein."]}

    return is_valid, errors
