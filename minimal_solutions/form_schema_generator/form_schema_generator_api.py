from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.form_schema_generator.form_schema_generator_validation import validate_form_schema_request

api_bp = Blueprint('form_schema_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/form_schema_generator', methods=['POST'])
def handle_form_schema_generator():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt."
        )

    is_valid, errors = validate_form_schema_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    fields = data.get('fields', [])
    
    schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {},
        "required": []
    }
    
    for field in fields:
        name = field['name']
        field_type = field['type']
        is_required = field.get('required', False)
        
        schema["properties"][name] = {
            "type": field_type
        }
        
        if 'description' in field:
            schema["properties"][name]["description"] = field["description"]
            
        if is_required:
            schema["required"].append(name)
            
    if not schema["required"]:
        del schema["required"]

    return success_response(data={
        "schema": schema
    })
