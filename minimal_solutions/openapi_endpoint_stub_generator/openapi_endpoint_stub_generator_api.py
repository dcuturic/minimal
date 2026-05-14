from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.openapi_endpoint_stub_generator.openapi_endpoint_stub_generator_validation import validate_openapi_request
import json
import yaml

api_bp = Blueprint('openapi_endpoint_stub_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/openapi_endpoint_stub_generator', methods=['POST'])
def handle_openapi_endpoint_stub_generator():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_openapi_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    path = data['path']
    method = data['method'].lower()
    summary = data['summary']
    request_fields = data.get('request_fields', [])

    if isinstance(request_fields, str):
        fields = [f.strip() for f in request_fields.split(',') if f.strip()]
    else:
        fields = request_fields

    properties = {field: {"type": "string"} for field in fields}

    stub = {
        path: {
            method: {
                "summary": summary,
                "responses": {
                    "200": {
                        "description": "Erfolgreiche Antwort",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "status": {"type": "string", "example": "success"},
                                        "data": {"type": "object"}
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    if method in ['post', 'put', 'patch'] and fields:
        stub[path][method]["requestBody"] = {
            "required": True,
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": properties,
                        "required": fields
                    }
                }
            }
        }
    elif fields:
        parameters = []
        for field in fields:
            parameters.append({
                "name": field,
                "in": "query",
                "required": True,
                "schema": {"type": "string"}
            })
        stub[path][method]["parameters"] = parameters

    return success_response(data={
        "openapi_stub": json.dumps(stub, indent=2),
        "yaml": yaml.dump({"paths": stub}, default_flow_style=False, sort_keys=False)
    })
