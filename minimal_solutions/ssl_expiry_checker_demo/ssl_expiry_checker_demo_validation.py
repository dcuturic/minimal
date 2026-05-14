import re

def validate_ssl_request(data):
    errors = []
    
    domain = data.get('domain', '')
    if not isinstance(domain, str):
        domain = ''
    domain = domain.strip()
    
    if not domain:
        errors.append("Das Feld 'domain' darf nicht leer sein.")
    elif len(domain) > 255:
        errors.append("Das Feld 'domain' darf maximal 255 Zeichen lang sein.")
    else:
        domain_regex = re.compile(
            r'^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$'
        )
        if not domain_regex.match(domain):
            errors.append("Das Feld 'domain' hat ein ungültiges Format.")
            
    return len(errors) == 0, errors
