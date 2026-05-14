from fastapi import APIRouter, Request
from app.response import ResponseBuilder
from .validation import validate_hosting_formatter_request

router = APIRouter()

@router.post("/api/minimal-solutions/hosting_formatter")
async def hosting_formatter_api(request: Request):
    try:
        data = await request.json()
    except Exception:
        data = {}

    is_valid, errors = validate_hosting_formatter_request(data)
    if not is_valid:
        return ResponseBuilder.error("Validierungsfehler", details=errors)

    source = data.get("source")
    config = data.get("config")
    mode = data.get("mode")

    result = {
        "source": source,
        "config": config,
        "mode": mode,
        "formatted_hosting": "Formatted Standard Web Hosting",
        "message": "Hosting successfully formatted."
    }

    return ResponseBuilder.success(result)
