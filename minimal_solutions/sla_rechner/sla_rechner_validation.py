from typing import Tuple, Dict
from datetime import datetime

def validate_sla_request(data: dict) -> Tuple[bool, Dict[str, str]]:
    errors = {}
    
    if not isinstance(data, dict):
        return False, {"request": "Invalid JSON format"}
        
    priority = data.get('priority')
    start_time = data.get('start_time')
    
    valid_priorities = ['p1', 'p2', 'p3', 'p4']
    
    if not priority:
        errors['priority'] = "Das Feld 'priority' ist erforderlich."
    elif priority not in valid_priorities:
        errors['priority'] = f"Das Feld 'priority' muss einer dieser Werte sein: {', '.join(valid_priorities)}."
        
    if not start_time:
        errors['start_time'] = "Das Feld 'start_time' ist erforderlich."
    else:
        try:
            datetime.fromisoformat(start_time)
        except ValueError:
            errors['start_time'] = "Das Feld 'start_time' muss ein gültiges ISO 8601 Datumsformat sein."
            
    return len(errors) == 0, errors
