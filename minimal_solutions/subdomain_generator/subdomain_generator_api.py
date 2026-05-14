from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.subdomain_generator.subdomain_generator_validation import validate_subdomain_request
import re

api_bp = Blueprint('subdomain_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/subdomain_generator', methods=['POST'])
def generate_subdomain():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_subdomain_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    name = data.get('name', '').strip()
    base_domain = data.get('base_domain', '').strip()
    
    # Normalize name to subdomain friendly format
    subdomain_prefix = name.lower()
    # Replace spaces with hyphens
    subdomain_prefix = re.sub(r'\s+', '-', subdomain_prefix)
    # Remove any character that isn't a-z, 0-9, or hyphen
    subdomain_prefix = re.sub(r'[^a-z0-9\-]', '', subdomain_prefix)
    # Remove multiple hyphens
    subdomain_prefix = re.sub(r'\-+', '-', subdomain_prefix)
    # Strip leading/trailing hyphens
    subdomain_prefix = subdomain_prefix.strip('-')
    
    if not subdomain_prefix:
        subdomain_prefix = "app" # Fallback if name was only special characters
        
    subdomains = [
        f"{subdomain_prefix}.{base_domain}",
        f"api.{subdomain_prefix}.{base_domain}",
        f"app.{subdomain_prefix}.{base_domain}",
        f"{subdomain_prefix}-app.{base_domain}",
        f"my{subdomain_prefix}.{base_domain}",
        f"{subdomain_prefix}hq.{base_domain}"
    ]

    return success_response(data={
        "subdomains": subdomains,
        "name": name,
        "base_domain": base_domain
    })
