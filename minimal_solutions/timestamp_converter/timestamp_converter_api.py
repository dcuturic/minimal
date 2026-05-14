from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.timestamp_converter.timestamp_converter_validation import validate_timestamp_request
from datetime import datetime, timezone
try:
    import zoneinfo
except ImportError:
    from backports import zoneinfo

api_bp = Blueprint('timestamp_converter_api', __name__)

@api_bp.route('/api/minimal-solutions/timestamp_converter', methods=['POST'])
def handle_timestamp_converter():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_timestamp_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    mode = data.get('mode')
    value = data.get('value')
    tz_string = data.get('timezone', 'UTC')
    
    if not tz_string:
        tz_string = 'UTC'

    try:
        tz = zoneinfo.ZoneInfo(tz_string)
    except Exception:
        tz = timezone.utc

    result = ""

    try:
        if mode == 'timestamp_to_date':
            try:
                ts = float(value)
                # If value is > 10^11, assume it's in milliseconds
                if ts > 100000000000:
                    ts = ts / 1000.0
                dt = datetime.fromtimestamp(ts, tz=tz)
                result = dt.isoformat()
            except ValueError:
                return error_response(
                    code=ErrorCodes.VALIDATION_ERROR,
                    message="Ungültiger Timestamp-Wert.",
                    details={"value": "Der Wert muss eine gültige Zahl sein."}
                )
                
        elif mode == 'date_to_timestamp':
            try:
                # Basic fromisoformat support
                dt_str = str(value).replace('Z', '+00:00')
                dt = datetime.fromisoformat(dt_str)
                if dt.tzinfo is None:
                    dt = dt.replace(tzinfo=tz)
                result = int(dt.timestamp() * 1000) # Returns milliseconds
            except ValueError:
                return error_response(
                    code=ErrorCodes.VALIDATION_ERROR,
                    message="Ungültiges Datumsformat.",
                    details={"value": "Das Datum muss im ISO-8601 Format sein (z.B. 2026-05-10T19:22:00)."}
                )
    except Exception:
        return error_response(
            code=ErrorCodes.INTERNAL_SERVER_ERROR,
            message="Interner Fehler beim Verarbeiten."
        )

    return success_response(data={
        "result": result
    })
