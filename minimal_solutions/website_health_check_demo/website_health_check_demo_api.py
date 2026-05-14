from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.website_health_check_demo.website_health_check_demo_validation import validate_health_check_request
import time
import urllib.request
import urllib.error

api_bp = Blueprint('website_health_check_demo_api', __name__)

@api_bp.route('/api/minimal-solutions/website_health_check_demo', methods=['POST'])
def check_website():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_health_check_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    url = data.get('url')
    
    start_time = time.time()
    status_code = None
    is_up = False
    
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            status_code = response.getcode()
            is_up = 200 <= status_code < 400
    except urllib.error.HTTPError as e:
        status_code = e.code
        # Consider a 403 or 401 as down or up depending on use-case, let's just say anything >= 400 is down for a simple check.
        is_up = False
    except urllib.error.URLError as e:
        status_code = 0
        is_up = False
    except Exception as e:
        status_code = 0
        is_up = False

    end_time = time.time()
    response_time_ms = int((end_time - start_time) * 1000)

    return success_response(data={
        "url": url,
        "is_up": is_up,
        "status_code": status_code,
        "response_time_ms": response_time_ms,
        "message": "Website is UP" if is_up else "Website is DOWN"
    })
