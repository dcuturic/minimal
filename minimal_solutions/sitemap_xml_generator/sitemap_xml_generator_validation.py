def validate_sitemap_xml_generator_input(data):
    errors = {}
    if not isinstance(data, dict):
        return False, {"payload": "Erwartet wurde ein JSON-Objekt."}
        
    if "urls" in data and not isinstance(data["urls"], (str, list)):
        errors["urls"] = "Das Feld 'urls' muss ein String oder eine Liste sein."
        
    if "changefreq" in data and not isinstance(data["changefreq"], str):
        errors["changefreq"] = "Das Feld 'changefreq' muss ein String sein."
        
    if "priority" in data and not isinstance(data["priority"], (str, int, float)):
        errors["priority"] = "Das Feld 'priority' muss eine Zahl oder ein String sein."
        
    if errors:
        return False, errors
    return True, {}
