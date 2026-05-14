from typing import Tuple, Dict

def validate_prompt_template_builder_request(data: dict) -> Tuple[bool, Dict[str, str]]:
    errors = {}
    
    if not isinstance(data, dict):
        return False, {"request": "Invalid JSON format"}
        
    goal = data.get('goal')
    variables = data.get('variables')
    constraints = data.get('constraints')
    
    if goal is None:
        errors['goal'] = "Das Feld 'goal' ist erforderlich."
    elif not isinstance(goal, str):
        errors['goal'] = "Das Feld 'goal' muss ein String sein."
    elif len(goal.strip()) == 0:
        errors['goal'] = "Das Feld 'goal' darf nicht leer sein."
        
    if variables is not None and not isinstance(variables, str):
        errors['variables'] = "Das Feld 'variables' muss ein String sein."
        
    if constraints is not None and not isinstance(constraints, str):
        errors['constraints'] = "Das Feld 'constraints' muss ein String sein."
        
    return len(errors) == 0, errors
