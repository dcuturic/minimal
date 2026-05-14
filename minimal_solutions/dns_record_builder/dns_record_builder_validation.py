from typing import Tuple, Dict

def validate_dns_record_request(data: dict) -> Tuple[bool, Dict[str, str]]:
    errors = {}
    
    if not isinstance(data, dict):
        return False, {"request": "Invalid JSON format"}
        
    record_type = data.get('type')
    name = data.get('name')
    value = data.get('value')
    ttl = data.get('ttl')
    
    if not record_type:
        errors['type'] = "Das Feld 'type' ist erforderlich."
    elif not isinstance(record_type, str):
        errors['type'] = "Das Feld 'type' muss ein String sein."
    elif record_type.upper() not in ['A', 'AAAA', 'CNAME', 'MX', 'TXT', 'NS', 'SRV', 'PTR']:
        errors['type'] = f"Der Typ '{record_type}' wird nicht unterstützt."
        
    if not name:
        errors['name'] = "Das Feld 'name' ist erforderlich."
    elif not isinstance(name, str):
        errors['name'] = "Das Feld 'name' muss ein String sein."
        
    if not value:
        errors['value'] = "Das Feld 'value' ist erforderlich."
    elif not isinstance(value, str):
        errors['value'] = "Das Feld 'value' muss ein String sein."
        
    if not ttl:
        errors['ttl'] = "Das Feld 'ttl' ist erforderlich."
    else:
        try:
            ttl_val = int(ttl)
            if ttl_val < 0:
                errors['ttl'] = "TTL muss eine positive Zahl sein."
        except ValueError:
            errors['ttl'] = "TTL muss eine gültige Zahl sein."
            
    return len(errors) == 0, errors
