from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.uuid_generator.uuid_generator_validation import validate_uuid_request
import uuid

api_bp = Blueprint('uuid_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/uuid_generator', methods=['POST'])
def generate_uuid():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_uuid_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    count = data.get('count')
    version = data.get('version')

    # Optional namespace and name for UUID v3/v5
    # If not provided, we might default to something or return an error, 
    # but the ticket just says count and version. 
    # Let's fallback to URL namespace if name is provided, else just fail or ignore.
    namespace = uuid.NAMESPACE_URL
    name = data.get('name', 'example.com')

    uuids = []
    for _ in range(count):
        if version == 1:
            uuids.append(str(uuid.uuid1()))
        elif version == 3:
            uuids.append(str(uuid.uuid3(namespace, name)))
        elif version == 4:
            uuids.append(str(uuid.uuid4()))
        elif version == 5:
            uuids.append(str(uuid.uuid5(namespace, name)))

    return success_response(data={"uuids": uuids})
