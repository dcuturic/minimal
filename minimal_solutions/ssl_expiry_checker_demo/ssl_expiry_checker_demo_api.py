from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.ssl_expiry_checker_demo.ssl_expiry_checker_demo_validation import validate_ssl_request
import ssl
import socket
from datetime import datetime

api_bp = Blueprint('ssl_expiry_checker_demo_api', __name__)

@api_bp.route('/api/minimal-solutions/ssl_expiry_checker_demo', methods=['POST'])
def check_ssl_expiry():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_ssl_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    domain = data.get('domain', '').strip()

    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                
        expiry_date_str = cert['notAfter']
        expiry_date = datetime.strptime(expiry_date_str, "%b %d %H:%M:%S %Y %Z")
        now = datetime.utcnow()
        
        days_remaining = (expiry_date - now).days
        is_valid_ssl = days_remaining > 0
        
        # formatting issuer to a dict if possible
        issuer_dict = {}
        for item in cert.get('issuer', []):
            for k, v in item:
                issuer_dict[k] = v

        return success_response(data={
            "domain": domain,
            "is_valid": is_valid_ssl,
            "days_remaining": days_remaining,
            "expiry_date": expiry_date.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "issuer": issuer_dict
        })
        
    except (socket.error, ssl.SSLError, Exception) as e:
        return success_response(data={
            "domain": domain,
            "is_valid": False,
            "days_remaining": 0,
            "expiry_date": None,
            "error_details": "Verbindung fehlgeschlagen oder kein gültiges SSL-Zertifikat gefunden."
        })
