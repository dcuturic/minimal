# Knowledge Base Card Generator

Minimal solution for generating knowledge base cards from raw text. This tool extracts structured information and creates concise cards, categorizing and giving titles to each piece of knowledge.

## Features
- Extracts structured knowledge base cards from unstructured text
- Allows specifying an optional category (default: "General")
- Returns an array of cards with `category`, `title`, and `content`
- API-first design for easy integration

## API Interface

The generator can be used externally via a REST API endpoint.

### Endpoint
`POST /api/minimal-solutions/knowledge_base_card_generator`

### Request Format
Content-Type: `application/json`

```json
{
  "source_text": "To reset your password, click on 'Forgot Password' on the login page and follow the link sent to your email. If you didn't receive the email, check your spam folder.",
  "category": "Troubleshooting"
}
```

**Parameters:**
- `source_text` (string, required): The raw text from which to extract the knowledge base cards. Must not be empty.
- `category` (string, optional): A category to assign to the generated cards. If not provided, defaults to "General".

### Response Format

The API returns a standardized response object with `status` and `data`.

**Success Example:**
```json
{
  "status": "success",
  "data": {
    "cards": [
      {
        "category": "Troubleshooting",
        "title": "Reset Password",
        "content": "Click 'Forgot Password' on the login page and follow the link sent to your email."
      },
      {
        "category": "Troubleshooting",
        "title": "Missing Password Reset Email",
        "content": "Check your spam folder if you didn't receive the password reset email."
      }
    ]
  }
}
```

**Error Example (Validation):**
```json
{
  "status": "error",
  "message": "Missing source_text."
}
```

## Integration
You can easily integrate this API into other applications or scripts by sending standard POST requests. The solution relies on an internal AI backend to generate the content but presents a clean and consistent output structure for developers.
