import time
from functools import wraps
from flask import request
from .responses import error_response, ErrorCodes

# Simple in-memory store for rate limiting: { "ip": [timestamp1, timestamp2, ...] }
# Note: In a production environment with multiple workers, use Redis or a similar key-value store.
_rate_limit_store = {}

def rate_limit(limit=10, window=60):
    """
    Rate limit decorator for API endpoints.
    
    Args:
        limit (int): Maximum number of requests allowed in the time window.
        window (int): Time window in seconds.
    """
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            ip = request.remote_addr
            now = time.time()
            
            if ip not in _rate_limit_store:
                _rate_limit_store[ip] = []
                
            # Filter out timestamps older than the window
            _rate_limit_store[ip] = [t for t in _rate_limit_store[ip] if now - t < window]
            
            if len(_rate_limit_store[ip]) >= limit:
                return error_response(
                    code=ErrorCodes.RATE_LIMIT_EXCEEDED,
                    message="Rate limit exceeded. Please try again later.",
                    details={"limit": limit, "window_seconds": window},
                    status_code=429
                )
                
            _rate_limit_store[ip].append(now)
            
            return f(*args, **kwargs)
        return wrapped
    return decorator
