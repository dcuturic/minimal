from typing import Tuple, Dict

def validate_cron_request(data: dict) -> Tuple[bool, Dict[str, str]]:
    errors = {}
    
    if not isinstance(data, dict):
        return False, {"request": "Invalid JSON format"}
        
    cron_expr = data.get('cron_expression')
    
    if not cron_expr:
        errors['cron_expression'] = "Das Feld 'cron_expression' ist erforderlich."
    elif not isinstance(cron_expr, str):
        errors['cron_expression'] = "Das Feld 'cron_expression' muss ein String sein."
    else:
        parts = cron_expr.strip().split()
        if len(parts) != 5:
            errors['cron_expression'] = "Ein Cron-Ausdruck muss aus genau 5 Teilen bestehen (Minute, Stunde, Tag, Monat, Wochentag)."
            
    return len(errors) == 0, errors
