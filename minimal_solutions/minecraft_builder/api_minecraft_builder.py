from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.minecraft_builder.validation_minecraft_builder import validate_minecraft_builder_request

api_bp = Blueprint('minecraft_builder_api', __name__)

@api_bp.route('/api/minimal-solutions/minecraft_builder', methods=['POST'])
def handle_minecraft_builder_request():
    if not request.is_json:
        return error_response(ErrorCodes.BAD_REQUEST, "Request must be JSON")

    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_minecraft_builder_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors,
            status_code=400
        )

    input_text = data.get("input_text")
    mode = data.get("mode")
    options = data.get("options", {})

    result_data = {
        "input_text": input_text,
        "mode": mode,
        "options": options,
        "status": "success",
        "message": f"Minecraft Builder request successfully processed for mode '{mode}'.",
        "result": {
            "blueprint_url": "https://example.com/blueprints/medieval_castle_1.5x.blueprint",
            "blocks_required": {
                "stone_bricks": 4500,
                "oak_wood": 1200,
                "glass_panes": 300
            },
            "estimated_build_time": "4 hours"
        }
    }

    return success_response(data=result_data)
