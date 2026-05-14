from flask import jsonify

class ErrorCodes:
    """Standardized error codes for API responses."""
    BAD_REQUEST = "BAD_REQUEST"
    UNAUTHORIZED = "UNAUTHORIZED"
    FORBIDDEN = "FORBIDDEN"
    NOT_FOUND = "NOT_FOUND"
    VALIDATION_ERROR = "VALIDATION_ERROR"
    INTERNAL_SERVER_ERROR = "INTERNAL_SERVER_ERROR"
    SERVICE_UNAVAILABLE = "SERVICE_UNAVAILABLE"
    RATE_LIMIT_EXCEEDED = "RATE_LIMIT_EXCEEDED"

def base_response(success: bool, data=None, error=None, warnings=None, meta=None, status_code=200):
    """Base structure for all API responses."""
    response = {
        "success": success,
        "data": data if data is not None else {},
        "error": error if error is not None else None,
        "warnings": warnings if warnings is not None else [],
        "meta": meta if meta is not None else {}
    }
    return jsonify(response), status_code

def success_response(data=None, warnings=None, meta=None, status_code=200):
    """
    Returns a standardized success response.
    """
    return base_response(
        success=True,
        data=data,
        warnings=warnings,
        meta=meta,
        status_code=status_code
    )

def error_response(code, message, details=None, warnings=None, meta=None, status_code=400):
    """
    Returns a standardized error response.
    """
    error_payload = {
        "code": code,
        "message": message,
        "details": details if details is not None else {}
    }
    return base_response(
        success=False,
        error=error_payload,
        warnings=warnings,
        meta=meta,
        status_code=status_code
    )
