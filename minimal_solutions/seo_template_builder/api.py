from fastapi import APIRouter, Request
from app.response import ResponseBuilder
from .validation import validate_seo_template_builder_request

router = APIRouter()

@router.post("/api/minimal-solutions/seo_template_builder")
async def seo_template_builder_api(request: Request):
    try:
        data = await request.json()
    except Exception:
        data = {}

    is_valid, errors = validate_seo_template_builder_request(data)
    if not is_valid:
        return ResponseBuilder.error("Validierungsfehler", details=errors)

    topic = data.get("topic")
    target = data.get("target")
    options = data.get("options", "")

    result = {
        "topic": topic,
        "target": target,
        "template_status": "success",
        "message": f"Template für '{topic}' erfolgreich erstellt."
    }

    if options:
        result["options_applied"] = options

    return ResponseBuilder.success(result)
