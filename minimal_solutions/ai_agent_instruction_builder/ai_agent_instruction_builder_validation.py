from typing import Tuple, Dict

def validate_ai_agent_instruction_builder_request(data: dict) -> Tuple[bool, Dict[str, str]]:
    errors = {}
    
    if not isinstance(data, dict):
        return False, {"request": "Invalid JSON format"}
        
    agent_name = data.get('agent_name')
    purpose = data.get('purpose')
    tools = data.get('tools')
    constraints = data.get('constraints')
    
    if agent_name is None:
        errors['agent_name'] = "Das Feld 'agent_name' ist erforderlich."
    elif not isinstance(agent_name, str):
        errors['agent_name'] = "Das Feld 'agent_name' muss ein String sein."
    elif len(agent_name.strip()) == 0:
        errors['agent_name'] = "Das Feld 'agent_name' darf nicht leer sein."
        
    if purpose is None:
        errors['purpose'] = "Das Feld 'purpose' ist erforderlich."
    elif not isinstance(purpose, str):
        errors['purpose'] = "Das Feld 'purpose' muss ein String sein."
    elif len(purpose.strip()) == 0:
        errors['purpose'] = "Das Feld 'purpose' darf nicht leer sein."

    if tools is not None and not isinstance(tools, str):
        errors['tools'] = "Das Feld 'tools' muss ein String sein."

    if constraints is not None and not isinstance(constraints, str):
        errors['constraints'] = "Das Feld 'constraints' muss ein String sein."
        
    return len(errors) == 0, errors
