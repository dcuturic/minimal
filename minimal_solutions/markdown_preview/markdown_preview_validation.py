def validate_input(data: dict) -> tuple[bool, dict]:
    errors = {}
    
    if not isinstance(data, dict):
        return False, {'base': 'Eingabe muss ein JSON-Objekt sein.'}
        
    if 'markdown_text' not in data:
        errors['markdown_text'] = 'Markdown-Text fehlt.'
    elif not isinstance(data['markdown_text'], str):
        errors['markdown_text'] = 'Markdown-Text muss ein String sein.'
    elif not data['markdown_text'].strip():
        errors['markdown_text'] = 'Markdown-Text darf nicht leer sein.'
        
    return len(errors) == 0, errors
