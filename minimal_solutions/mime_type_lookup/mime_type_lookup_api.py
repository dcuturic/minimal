from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.mime_type_lookup.mime_type_lookup_validation import validate_mime_type_request
import mimetypes

api_bp = Blueprint('mime_type_lookup_api', __name__)

@api_bp.route('/api/minimal-solutions/mime_type_lookup', methods=['POST'])
def handle_mime_type_lookup():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_mime_type_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    query = data.get('query', '').strip()
    results = []

    mimetypes.init()
    
    if '/' in query and len(query.split('/')) == 2:
        extensions = mimetypes.guess_all_extensions(query)
        if extensions:
            unique_exts = sorted(list(set(extensions)))
            results.append({
                "extension": ", ".join(unique_exts),
                "mime_type": query,
                "description": "Gefunden über MIME Type"
            })
    else:
        filename = query
        if not filename.startswith('.') and '.' not in filename:
            filename = f".{filename}"
            
        mime_type, _ = mimetypes.guess_type(f"file{filename}")
        
        if mime_type:
            extensions = mimetypes.guess_all_extensions(mime_type)
            unique_exts = sorted(list(set(extensions))) if extensions else [filename]
            
            results.append({
                "extension": ", ".join(unique_exts),
                "mime_type": mime_type,
                "description": "Gefunden über Dateiendung"
            })

    return success_response(data={"results": results})
