# Error Message Explainer

The Error Message Explainer is a minimal solution on the CraftHoster platform that translates cryptic error messages into easy-to-understand causes and actionable resolution steps.

## External API Usage

You can seamlessly integrate the Error Message Explainer into your own applications by using our REST API endpoint. The endpoint processes the provided error message and an optional context to return specific causes and steps to resolve the issue.

**Endpoint:**
`POST /api/minimal-solutions/error_message_explainer`

### Request Format

The API expects a JSON payload with the following fields:
- `error_text` (string, required): The raw error message you want explained.
- `context` (string, optional): Additional context, such as the framework, language, or environment (e.g., "React", "Docker", "Python").

**Example Request:**
```json
{
  "error_text": "TypeError: Cannot read properties of undefined (reading 'map')",
  "context": "React"
}
```

### Response Format

The API returns a JSON response containing a `status` and `data` object. The `data` object contains two lists: `causes` and `steps`.

**Example Response:**
```json
{
  "status": "success",
  "data": {
    "causes": [
      "The variable you are calling '.map()' on is undefined."
    ],
    "steps": [
      "Ensure the data is fetched or passed correctly.",
      "Use optional chaining: 'variable?.map()'."
    ]
  }
}
```

### Integration Notes
- Make sure to set the `Content-Type: application/json` header in your HTTP request.
- The `error_text` must be a valid string, or the API will return a validation error.
- The explainer will do its best to provide actionable feedback based on the provided error message and context.
