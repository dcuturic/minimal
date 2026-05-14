from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.release_notes_generator.release_notes_generator_validation import validate_release_notes_request

api_bp = Blueprint('release_notes_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/release_notes_generator', methods=['POST'])
def handle_release_notes():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_release_notes_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    version = data.get('version', '')
    features = data.get('features') or []
    fixes = data.get('fixes') or []
    breaking_changes = data.get('breaking_changes') or []

    try:
        notes = []
        notes.append(f"# Release Notes - {version}")
        
        has_content = False
        
        if features and any(f.strip() for f in features):
            notes.append("\n## 🚀 Features")
            for feature in features:
                if feature.strip():
                    notes.append(f"- {feature.strip()}")
            has_content = True
            
        if fixes and any(f.strip() for f in fixes):
            notes.append("\n## 🐛 Bug Fixes")
            for fix in fixes:
                if fix.strip():
                    notes.append(f"- {fix.strip()}")
            has_content = True
            
        if breaking_changes and any(b.strip() for b in breaking_changes):
            notes.append("\n## ⚠️ Breaking Changes")
            for change in breaking_changes:
                if change.strip():
                    notes.append(f"- {change.strip()}")
            has_content = True
            
        if not has_content:
            notes.append("\n*Keine Änderungen für dieses Release angegeben.*")
            
        result = "\n".join(notes)
        
        return success_response(data={"result": result})
    except Exception as e:
        return error_response(
            code=ErrorCodes.INTERNAL_SERVER_ERROR,
            message="Interner Fehler beim Verarbeiten."
        )
