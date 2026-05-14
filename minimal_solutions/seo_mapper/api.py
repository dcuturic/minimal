from fastapi import APIRouter, Request
from app.response import ResponseBuilder
from .validation import validate_seo_mapper_request

router = APIRouter()

@router.post("/api/minimal-solutions/seo_mapper")
async def seo_mapper_api(request: Request):
    try:
        data = await request.json()
    except Exception:
        data = {}

    is_valid, errors = validate_seo_mapper_request(data)
    if not is_valid:
        return ResponseBuilder.error("Validierungsfehler", details=errors)

    topic = data.get("topic")
    target = data.get("target")
    options = data.get("options", "")

    # Mapped dummy result
    result = {
        "topic": topic,
        "target": target,
        "mapped_status": "success",
        "message": f"Daten für '{topic}' erfolgreich gemappt."
    }

    if options:
        result["options_applied"] = options

    return ResponseBuilder.success(result)
