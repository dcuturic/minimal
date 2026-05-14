# Prompt Template Builder

This is a minimal solution to quickly generate structured prompt templates for Large Language Models based on a specified goal, variables, and constraints.

## Features
- **Goal Definition**: Define the main objective of the prompt.
- **Variable Injection**: Specify dynamic placeholders (e.g., `product_name`, `target_audience`).
- **Constraints Handling**: Add specific rules (e.g., tone, length, format).
- **API Access**: Use the REST API to integrate prompt generation into your applications.

## API Usage

You can generate prompt templates dynamically by sending a `POST` request to the API endpoint.

**Endpoint:**
`POST /api/minimal-solutions/prompt_template_builder`

### Request Example
```json
{
  "goal": "Write a marketing email",
  "variables": "product_name, target_audience",
  "constraints": "Keep it under 200 words, use an excited tone"
}
```

### Response Example
```json
{
  "status": "success",
  "data": {
    "prompt_template": "Your goal is: Write a marketing email.\n\nHere are the specific constraints to follow:\n- Keep it under 200 words, use an excited tone\n\nPlease incorporate the following variables into your response:\n- {product_name}\n- {target_audience}\n\nBegin your response now:"
  }
}
```

## Setup & Integration
- The user interface is available at `/minimal-solutions/prompt_template_builder`
- Core logic is encapsulated within `prompt_template_builder_api.py` and `prompt_template_builder_validation.py`.
