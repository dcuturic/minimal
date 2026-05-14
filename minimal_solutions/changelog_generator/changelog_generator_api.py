from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.changelog_generator.changelog_generator_validation import validate_changelog_generator_request

api_bp = Blueprint('changelog_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/changelog_generator', methods=['POST'])
def handle_changelog_generator():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_changelog_generator_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    version = data.get('version', '').strip()
    date_str = data.get('date', '').strip()
    changes = data.get('changes')

    changes_list = []
    if isinstance(changes, str):
        lines = [line.strip() for line in changes.split('\n') if line.strip()]
        for line in lines:
            if line.startswith('- ') or line.startswith('* '):
                changes_list.append(line)
            else:
                changes_list.append(f"- {line}")
    elif isinstance(changes, list):
        for item in changes:
            if isinstance(item, str) and item.strip():
                line = item.strip()
                if line.startswith('- ') or line.startswith('* '):
                    changes_list.append(line)
                else:
                    changes_list.append(f"- {line}")

    changelog_lines = [
        f"## [{version}] - {date_str}",
        "### Changes",
        *changes_list
    ]

    changelog = "\n".join(changelog_lines)

    return success_response(data={
        "result": changelog
    })
