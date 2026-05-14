from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from app.validation import Validator

api_bp = Blueprint('json_schema_validator_demo_api', __name__, url_prefix='/api/minimal-solutions/json_schema_validator_demo')

@api_bp.route('', methods=['POST'])
def validate_json_schema():
    data = request.get_json(silent=True)
    if not data:
        return error_response(ErrorCodes.BAD_REQUEST, "Ungültiges oder fehlendes JSON-Payload")

    # The UI sends parsed JSON objects/arrays directly, not strings.
    # Therefore, we just check if they are present.
    rules = {
        "json_text": {"required": True},
        "schema_text": {"required": True}
    }
    
    is_valid, validation_errors = Validator.validate(data, rules)
    if not is_valid:
        return error_response(ErrorCodes.VALIDATION_ERROR, "Validierungsfehler", details=validation_errors)

    json_data = data.get("json_text")
    schema_data = data.get("schema_text")

    try:
        import jsonschema
        from jsonschema.exceptions import ValidationError, SchemaError
        
        try:
            jsonschema.validate(instance=json_data, schema=schema_data)
            return success_response(data={
                "is_valid": True,
                "errors": []
            })
        except ValidationError as e:
            # e.path is a deque, convert to list and then to string path
            path = " -> ".join([str(p) for p in e.path]) if e.path else "root"
            error_msg = f"Fehler bei '{path}': {e.message}"
            return success_response(data={
                "is_valid": False,
                "errors": [error_msg]
            })
        except SchemaError as e:
            return success_response(data={
                "is_valid": False,
                "errors": [f"Ungültiges Schema: {e.message}"]
            })
    except ImportError:
        # Fallback if jsonschema is not installed
        # We simulate a simple check or return an error. Since we are told not to use external services
        # and we must do this minimal, returning an error is fine, or we could just return a warning.
        return error_response(ErrorCodes.INTERNAL_SERVER_ERROR, "Die 'jsonschema' Bibliothek ist nicht installiert.")
