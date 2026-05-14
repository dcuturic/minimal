from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.docker_compose_service_viewer.docker_compose_service_viewer_validation import validate_docker_compose_service_viewer_request

api_bp = Blueprint('docker_compose_service_viewer_api', __name__)

def parse_yaml_fallback(text):
    services = []
    lines = text.split('\n')
    in_services = False
    current_service = None
    service_data = {}
    current_key = None
    
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            continue
            
        indent = len(line) - len(line.lstrip())
        
        if indent == 0 and stripped == 'services:':
            in_services = True
            current_service = None
            continue
        elif indent == 0 and in_services and stripped.endswith(':'):
            in_services = False
            if current_service:
                service_data['name'] = current_service
                services.append(service_data)
                current_service = None
                service_data = {}
            continue
            
        if in_services:
            if indent > 0 and indent <= 4 and stripped.endswith(':'):
                if current_service:
                    service_data['name'] = current_service
                    services.append(service_data)
                current_service = stripped[:-1]
                service_data = {'image': 'N/A', 'ports': [], 'volumes': [], 'build': None}
                current_key = None
            elif current_service and indent > 2:
                if ':' in stripped:
                    key, val = stripped.split(':', 1)
                    key = key.strip()
                    val = val.strip()
                    if not val and stripped.endswith(':'):
                        current_key = key
                    else:
                        current_key = None
                        if key == 'image':
                            service_data['image'] = val.strip("'\"")
                        elif key == 'build':
                            service_data['build'] = val.strip("'\"")
                elif stripped.startswith('-') and current_key:
                    val = stripped[1:].strip()
                    if current_key == 'ports':
                        service_data['ports'].append(val.strip("'\""))
                    elif current_key == 'volumes':
                        service_data['volumes'].append(val.strip("'\""))
    
    if current_service:
        service_data['name'] = current_service
        services.append(service_data)
        
    return services

@api_bp.route('/api/minimal-solutions/docker_compose_service_viewer', methods=['POST'])
def docker_compose_service_viewer():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt."
        )

    is_valid, errors = validate_docker_compose_service_viewer_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    compose_yaml = data.get('compose_yaml', '')
    
    try:
        import yaml
        
        try:
            parsed_yaml = yaml.safe_load(compose_yaml)
            
            if not isinstance(parsed_yaml, dict):
                return error_response(
                    code=ErrorCodes.BAD_REQUEST,
                    message="Das YAML muss ein Dictionary auf oberster Ebene sein."
                )

            services_dict = parsed_yaml.get('services')
            if not services_dict or not isinstance(services_dict, dict):
                return error_response(
                    code=ErrorCodes.BAD_REQUEST,
                    message="Keine 'services' Sektion im YAML gefunden oder ungültiges Format."
                )
                
            services = []
            for service_name, service_data in services_dict.items():
                if not isinstance(service_data, dict):
                    service_data = {}
                    
                services.append({
                    "name": service_name,
                    "image": service_data.get('image', 'N/A'),
                    "ports": service_data.get('ports', []),
                    "volumes": service_data.get('volumes', []),
                    "build": service_data.get('build', None)
                })
        except yaml.YAMLError as e:
            return error_response(
                code=ErrorCodes.BAD_REQUEST,
                message="Ungültiges YAML Format.",
                details={"error": str(e)}
            )
            
    except ImportError:
        # Fallback to simple parser if pyyaml is not installed
        try:
            services = parse_yaml_fallback(compose_yaml)
            if not services:
                return error_response(
                    code=ErrorCodes.BAD_REQUEST,
                    message="Keine 'services' Sektion im YAML gefunden oder ungültiges Format."
                )
        except Exception as e:
            return error_response(
                code=ErrorCodes.INTERNAL_ERROR,
                message="Ein unerwarteter Fehler ist aufgetreten.",
                details={"error": str(e)}
            )
            
    except Exception as e:
        return error_response(
            code=ErrorCodes.INTERNAL_ERROR,
            message="Ein unerwarteter Fehler ist aufgetreten.",
            details={"error": str(e)}
        )

    return success_response(data={"services": services})
