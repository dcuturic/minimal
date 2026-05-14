# Support Ticket Summarizer

Minimal-Lösung für Support Ticket Summarizer.

## External Usage

This minimal solution provides a REST API endpoint to automatically summarize support tickets into a clear Problem, Cause, and Next Steps format. It can be integrated into external systems such as Zendesk, Jira Service Desk, or custom helpdesk software.

### API Endpoint

**URL:** `/api/minimal-solutions/support_ticket_summarizer`
**Method:** `POST`
**Content-Type:** `application/json`

### Request Example

```json
{
  "ticket_text": "Hi, I can't login to my account. It says 'Invalid password'. Please help."
}
```

### Response Example

```json
{
  "status": "success",
  "data": {
    "problem": "User cannot login, receives 'Invalid password' error.",
    "cause": "Incorrect password entered or account locked out.",
    "next_steps": [
      "Send password reset link to user's email.",
      "Check if account is locked out and unlock if necessary."
    ]
  }
}
```
