from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.meeting_notes_formatter.meeting_notes_formatter_validation import validate_meeting_notes_request

api_bp = Blueprint('meeting_notes_formatter_api', __name__)

@api_bp.route('/api/minimal-solutions/meeting_notes_formatter', methods=['POST'])
def format_meeting_notes():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_meeting_notes_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    notes = data.get("notes", "")
    
    lines = notes.split('\n')
    formatted_lines = []
    action_items = []
    
    for line in lines:
        line = line.strip()
        if not line:
            formatted_lines.append("")
            continue
            
        # Normalize bullets
        if line.startswith("- ") or line.startswith("* "):
            line = "• " + line[2:].strip().capitalize()
        else:
            # Capitalize first character
            if len(line) > 0:
                line = line[0].upper() + line[1:]
                
        # Detect action items
        upper_line = line.upper()
        if "TODO:" in upper_line or "ACTION:" in upper_line:
            action_items.append(line)
            
        formatted_lines.append(line)
        
    formatted_notes = "\n".join(formatted_lines)
    
    return success_response(data={
        "formatted_notes": formatted_notes,
        "action_items": action_items,
        "original_length": len(notes),
        "formatted_length": len(formatted_notes)
    })
