def validate_access_role_matrix_request(data):
    if not isinstance(data, dict):
        return False, ["Payload must be a JSON object."]
    
    if 'roles' not in data:
        return False, ["Missing required field: 'roles'."]
        
    if 'permissions' not in data:
        return False, ["Missing required field: 'permissions'."]
        
    roles = data.get('roles')
    if not isinstance(roles, list):
        return False, ["'roles' must be a list."]
        
    permissions = data.get('permissions')
    if not isinstance(permissions, list):
        return False, ["'permissions' must be a list."]
        
    errors = []
    
    for i, role in enumerate(roles):
        if not isinstance(role, str) or not role.strip():
            errors.append(f"Role at index {i} must be a non-empty string.")
            
    for i, perm in enumerate(permissions):
        if not isinstance(perm, str) or not perm.strip():
            errors.append(f"Permission at index {i} must be a non-empty string.")
            
    if errors:
        return False, errors
        
    return True, []
