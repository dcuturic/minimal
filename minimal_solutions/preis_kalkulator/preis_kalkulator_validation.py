def validate_preis_kalkulator_request(data):
    errors = {}
    if not data:
        return False, {"payload": "Invalid JSON payload"}
    
    # base_price
    if 'base_price' not in data:
        errors['base_price'] = "Basispreis ist erforderlich."
    else:
        try:
            base_price = float(data['base_price'])
            if base_price < 0:
                errors['base_price'] = "Basispreis darf nicht negativ sein."
        except ValueError:
            errors['base_price'] = "Basispreis muss eine Zahl sein."
            
    # margin
    if 'margin' not in data:
        errors['margin'] = "Marge ist erforderlich."
    else:
        try:
            margin = float(data['margin'])
            if margin < 0:
                errors['margin'] = "Marge darf nicht negativ sein."
        except ValueError:
            errors['margin'] = "Marge muss eine Zahl sein."

    # discount
    if 'discount' not in data:
        errors['discount'] = "Rabatt ist erforderlich."
    else:
        try:
            discount = float(data['discount'])
            if discount < 0 or discount > 100:
                errors['discount'] = "Rabatt muss zwischen 0 und 100 liegen."
        except ValueError:
            errors['discount'] = "Rabatt muss eine Zahl sein."

    # markup
    if 'markup' not in data:
        errors['markup'] = "Aufschlag ist erforderlich."
    else:
        try:
            markup = float(data['markup'])
            if markup < 0:
                errors['markup'] = "Aufschlag darf nicht negativ sein."
        except ValueError:
            errors['markup'] = "Aufschlag muss eine Zahl sein."
            
    if errors:
        return False, errors
    return True, None
