# Word Replacer

A simple, minimal solution for replacing specific words or phrases in a text.

## API Documentation

This tool provides a simple RESTful API endpoint to replace words programmatically.

**Endpoint:** `POST /api/minimal-solutions/word_replacer`

### Parameters (JSON Body)

- `text` (string, required): The original text in which words should be replaced.
- `search` (string, required): The word or phrase to look for.
- `replace` (string, optional, defaults to ""): The word or phrase to replace it with.
- `case_sensitive` (boolean, optional, defaults to false): Whether the search should be case-sensitive.

### Request Example

```javascript
fetch('/api/minimal-solutions/word_replacer', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
        "text": "Hello world, hello universe!",
        "search": "hello",
        "replace": "Hi",
        "case_sensitive": false
    })
});
```

### Response Example

```json
{
    "status": "success",
    "data": {
        "result_text": "Hi world, Hi universe!",
        "replacement_count": 2
    }
}
```
