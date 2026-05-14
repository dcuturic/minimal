def validate_robots_txt_generator_input(data):
    errors = {}
    if not isinstance(data, dict):
        return False, {"payload": "Erwartet wurde ein JSON-Objekt."}
        
    if "allow" in data and not isinstance(data["allow"], str):
        errors["allow"] = "Das Feld 'allow' muss ein String sein."
        
    if "disallow" in data and not isinstance(data["disallow"], str):
        errors["disallow"] = "Das Feld 'disallow' muss ein String sein."
        
    if "sitemap_url" in data and not isinstance(data["sitemap_url"], str):
        errors["sitemap_url"] = "Das Feld 'sitemap_url' muss ein String sein."

    if "user_agent" in data and not isinstance(data["user_agent"], str):
        errors["user_agent"] = "Das Feld 'user_agent' muss ein String sein."
        
    if errors:
        return False, errors
    return True, {}
