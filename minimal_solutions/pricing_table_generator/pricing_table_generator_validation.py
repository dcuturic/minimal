def validate_pricing_table_generator_input(data):
    errors = {}
    
    if not isinstance(data, dict):
        return False, {"_root": "Eingabe muss ein Objekt sein."}
        
    plans = data.get('plans')
    if plans is None:
        errors['plans'] = "Plans ist ein Pflichtfeld."
    elif not isinstance(plans, list):
        errors['plans'] = "Plans muss eine Liste sein."
    elif len(plans) == 0:
        errors['plans'] = "Plans darf nicht leer sein."
    else:
        for idx, plan in enumerate(plans):
            if not isinstance(plan, dict):
                errors[f'plans[{idx}]'] = "Plan muss ein Objekt sein."
            else:
                if 'name' not in plan or not isinstance(plan['name'], str) or not plan['name'].strip():
                    errors[f'plans[{idx}].name'] = "Name des Plans ist erforderlich."
                if 'price' not in plan and plan.get('price') != 0:
                    errors[f'plans[{idx}].price'] = "Preis des Plans ist erforderlich."
            
    return len(errors) == 0, errors
