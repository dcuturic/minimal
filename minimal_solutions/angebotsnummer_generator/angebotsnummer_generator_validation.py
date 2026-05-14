def validate_angebotsnummer_request(data):
    if not isinstance(data, dict):
        return False, {"error": "Erwartet wurde ein JSON-Objekt/Dictionary."}
    
    errors = {}
    
    prefix = data.get('prefix')
    date = data.get('date')
    customer_short = data.get('customer_short')
    number = data.get('number')
    
    if prefix is not None and not isinstance(prefix, str):
        errors['prefix'] = "Prefix muss ein String sein."
        
    if date is not None and not isinstance(date, str):
        errors['date'] = "Datum muss ein String sein."
        
    if customer_short is not None and not isinstance(customer_short, str):
        errors['customer_short'] = "Kürzel (customer_short) muss ein String sein."
        
    if number is None or not isinstance(number, (str, int)):
        errors['number'] = "Nummer ist erforderlich und muss ein String oder eine Zahl sein."
        
    if errors:
        return False, errors
        
    return True, {}
