from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes

api_bp = Blueprint('minecraft_preview_api', __name__)

@api_bp.route('/api/minimal-solutions/minecraft_preview', methods=['POST'])
def handle_request():
    if not request.is_json:
        return error_response(ErrorCodes.BAD_REQUEST, "Request must be JSON")

    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    input_text = data.get("input_text", "")
    options = data.get("options", {})
    mode = data.get("mode", "2d")

    result_data = {
        "input_text": input_text,
        "options": options,
        "mode": mode,
        "preview_url": "https://example.com/preview/minecraft_stone",
        "status": "success",
        "message": "Minecraft Vorschau erfolgreich generiert."
    }

    return success_response(data=result_data)
