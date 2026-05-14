def validate_mwst_request(data):
    errors = {}
    if not data:
        return False, {"payload": "Invalid JSON payload"}
    
    if 'amount' not in data:
        errors['amount'] = "Betrag ist erforderlich."
    else:
        try:
            amount = float(data['amount'])
            if amount < 0:
                errors['amount'] = "Betrag darf nicht negativ sein."
        except ValueError:
            errors['amount'] = "Betrag muss eine Zahl sein."
            
    if 'mode' not in data:
        errors['mode'] = "Modus ist erforderlich."
    elif data['mode'] not in ['net_to_gross', 'gross_to_net']:
        errors['mode'] = "Ungültiger Modus. Erlaubt sind 'net_to_gross' oder 'gross_to_net'."
        
    if 'vat_rate' not in data:
        errors['vat_rate'] = "Mehrwertsteuersatz ist erforderlich."
    else:
        try:
            vat_rate = float(data['vat_rate'])
            if vat_rate < 0:
                errors['vat_rate'] = "Mehrwertsteuersatz darf nicht negativ sein."
        except ValueError:
            errors['vat_rate'] = "Mehrwertsteuersatz muss eine Zahl sein."
        
    if errors:
        return False, errors
    return True, None
