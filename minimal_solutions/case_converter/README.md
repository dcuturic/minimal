# Case Converter

Eine Minimal-Lösung, um Texte in verschiedene Schreibweisen (z.B. UPPERCASE, lowercase, camelCase, snake_case) zu konvertieren.

## UI-Verwendung
Die Lösung kann in der UI unter `/minimal-solutions/case_converter` aufgerufen werden. 

## API-Verwendung
Die Funktionalität kann auch extern über die REST-API genutzt werden.

**Endpoint:** `POST /api/minimal-solutions/case_converter`

### Request-Beispiel
```json
{
  "text": "Hello world",
  "target_case": "uppercase"
}
```

### Response-Beispiel
```json
{
  "status": "success",
  "data": {
    "result": "HELLO WORLD"
  }
}
```

**Unterstützte Formate (target_case):**
- `uppercase`
- `lowercase`
- `titlecase`
- `camelcase`
- `snakecase`
- `kebabcase`
- `pascalcase`
