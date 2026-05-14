from typing import Tuple, Dict

def validate_priority_request(data: dict) -> Tuple[bool, Dict[str, str]]:
    errors = {}
    
    if not isinstance(data, dict):
        return False, {"request": "Invalid JSON format"}
        
    ticket_text = data.get('ticket_text')
    
    if ticket_text is None:
        errors['ticket_text'] = "Das Feld 'ticket_text' ist erforderlich."
    elif not isinstance(ticket_text, str):
        errors['ticket_text'] = "Das Feld 'ticket_text' muss ein String sein."
    elif len(ticket_text.strip()) == 0:
        errors['ticket_text'] = "Das Feld 'ticket_text' darf nicht leer sein."
        
    return len(errors) == 0, errors
