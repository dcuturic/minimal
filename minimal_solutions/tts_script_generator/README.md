# TTS Script Generator - Minimal Solution

This is the documentation for the **TTS Script Generator** minimal solution.

## API Usage

The TTS Script Generator can be integrated externally via our REST API.

### Endpoint

`POST /api/minimal-solutions/tts_script_generator`

### Request Format

Send a JSON payload with the following fields:
- `topic` (string, required): The topic or subject for the script.
- `voice_style` (string, required): The tone/style of the voice (e.g., professional, energetic, calm, funny, dramatic).
- `duration` (string, required): The expected duration (e.g., 15s, 30s, 60s).

**Example Request:**
```json
{
  "topic": "Benefits of AI",
  "voice_style": "professional",
  "duration": "30s"
}
```

### Response Format

The API returns a standardized JSON response containing the generated script.

**Example Response:**
```json
{
  "status": "success",
  "data": {
    "script": "Artificial Intelligence is transforming our world. In healthcare, algorithms analyze data to detect diseases earlier than ever. By optimizing processes..."
  }
}
```

### External Integration

To use this interface externally, simply make a POST request with an HTTP client (like cURL, Axios, or `fetch`) to the endpoint passing the required JSON payload. Ensure that the `Content-Type: application/json` header is set.
