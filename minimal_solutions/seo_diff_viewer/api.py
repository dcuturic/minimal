from fastapi import APIRouter, Request
from app.response import ResponseBuilder
from .validation import validate_seo_diff_viewer_request

router = APIRouter()

@router.post("/api/minimal-solutions/seo_diff_viewer")
async def seo_diff_viewer_api(request: Request):
    try:
        data = await request.json()
    except Exception:
        data = {}

    is_valid, errors = validate_seo_diff_viewer_request(data)
    if not is_valid:
        return ResponseBuilder.error("Validierungsfehler", details=errors)

    topic = data.get("topic")
    target = data.get("target")
    options = data.get("options", "")

    # Simulated diff calculation result
    result = {
        "topic": topic,
        "target": target,
        "diff_status": "success",
        "message": f"Diff für '{topic}' erfolgreich berechnet."
    }

    if options:
        result["options_applied"] = options

    return ResponseBuilder.success(result)
