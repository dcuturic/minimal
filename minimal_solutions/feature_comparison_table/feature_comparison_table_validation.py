def validate_feature_comparison_table_input(data):
    errors = {}
    
    if not isinstance(data, dict):
        return False, {"_root": "Eingabe muss ein Objekt sein."}
        
    features = data.get('features')
    if features is None:
        errors['features'] = "Features ist ein Pflichtfeld."
    elif not isinstance(features, list):
        errors['features'] = "Features muss eine Liste sein."
        
    items = data.get('items')
    if items is None:
        errors['items'] = "Items ist ein Pflichtfeld."
    elif not isinstance(items, list):
        errors['items'] = "Items muss eine Liste sein."
    else:
        for idx, item in enumerate(items):
            if not isinstance(item, dict):
                errors[f'items[{idx}]'] = "Item muss ein Objekt sein."
            elif 'name' not in item or not isinstance(item.get('name'), str) or not item['name'].strip():
                errors[f'items[{idx}].name'] = "Name des Items ist erforderlich."

    return len(errors) == 0, errors
