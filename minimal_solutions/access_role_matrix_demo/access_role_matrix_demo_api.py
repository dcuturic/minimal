from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.access_role_matrix_demo.access_role_matrix_demo_validation import validate_access_role_matrix_request

api_bp = Blueprint('access_role_matrix_demo_api', __name__)

@api_bp.route('/api/minimal-solutions/access_role_matrix_demo', methods=['POST'])
def handle_access_role_matrix_demo():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt."
        )

    is_valid, errors = validate_access_role_matrix_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    roles = data.get('roles', [])
    permissions = data.get('permissions', [])
    
    matrix = []
    
    for role in roles:
        role_lower = role.lower()
        role_perms = {}
        for p in permissions:
            p_lower = p.lower()
            is_checked = False
            
            if role_lower == 'admin':
                is_checked = True
            elif role_lower == 'editor' and p_lower in ['read', 'write']:
                is_checked = True
            elif role_lower == 'viewer' and p_lower == 'read':
                is_checked = True
                
            role_perms[p] = is_checked
            
        matrix.append({
            "role": role,
            "permissions": role_perms
        })

    return success_response(data={
        "matrix": matrix
    })
