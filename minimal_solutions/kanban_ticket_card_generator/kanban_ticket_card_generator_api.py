from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.kanban_ticket_card_generator.kanban_ticket_card_generator_validation import validate_kanban_ticket_request

api_bp = Blueprint('kanban_ticket_card_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/kanban_ticket_card_generator', methods=['POST'])
def generate_kanban_card():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_kanban_ticket_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    title = data.get("title", "").strip()
    description = data.get("description", "")
    priority = data.get("priority", "medium")
    status = data.get("status", "todo")

    card_data = {
        "title": title,
        "description": description,
        "priority": priority,
        "status": status
    }
    
    html_preview = f"""<div class="ktcg-card">
    <div class="ktcg-card-header">
        <h3 class="ktcg-card-title">{title}</h3>
        <span class="ktcg-card-badge status-{status}">{status.upper().replace('_', ' ')}</span>
    </div>
    <div class="ktcg-card-desc">
        {description if description else 'No description provided.'}
    </div>
    <div class="ktcg-card-footer">
        <span>Priority: <strong class="priority-{priority}">{priority.capitalize()}</strong></span>
    </div>
</div>"""

    return success_response(data={
        "card": card_data,
        "html_preview": html_preview
    })
