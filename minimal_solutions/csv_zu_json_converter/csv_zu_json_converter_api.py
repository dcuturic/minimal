import csv
import io
import json
from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.csv_zu_json_converter.csv_zu_json_converter_validation import validate_input

api_bp = Blueprint('csv_zu_json_converter_api', __name__)

@api_bp.route('/api/minimal-solutions/csv_zu_json_converter', methods=['POST'])
def convert_csv_to_json():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_input(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    csv_text = data['csv_text'].strip()
    delimiter = data.get('delimiter', ',')
    
    has_header = data.get('has_header', True)
    if isinstance(has_header, str):
        has_header = has_header.lower() == 'true'

    try:
        f = io.StringIO(csv_text)
        if has_header:
            reader = csv.DictReader(f, delimiter=delimiter)
            result = list(reader)
        else:
            reader = csv.reader(f, delimiter=delimiter)
            result = list(reader)
            
        return success_response(data={
            "json_data": result,
            "parsed_count": len(result)
        })
    except csv.Error as e:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Fehler beim Parsen der CSV-Datei.",
            details={"csv_error": str(e)}
        )
    except Exception as e:
        return error_response(
            code=ErrorCodes.INTERNAL_ERROR,
            message="Ein unerwarteter Fehler ist aufgetreten.",
            details={"error": str(e)}
        )
