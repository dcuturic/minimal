from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.json_zu_csv_converter.json_zu_csv_converter_validation import validate_json_zu_csv_converter_request
import json
import csv
import io

api_bp = Blueprint('json_zu_csv_converter_api', __name__)

@api_bp.route('/api/minimal-solutions/json_zu_csv_converter', methods=['POST'])
def convert_json_to_csv():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_json_zu_csv_converter_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    json_text = data.get('json_text')
    delimiter = data.get('delimiter', ',')
    if not delimiter:
        delimiter = ','

    try:
        parsed_json = json.loads(json_text)
    except json.JSONDecodeError as e:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Ungültiges JSON-Format",
            details={"json_text": f"Fehler beim Parsen des JSON: {str(e)}"}
        )

    if not isinstance(parsed_json, list):
        if isinstance(parsed_json, dict):
            parsed_json = [parsed_json]
        else:
            return error_response(
                code=ErrorCodes.VALIDATION_ERROR,
                message="Ungültiges JSON-Format",
                details={"json_text": "JSON muss ein Array von Objekten oder ein einzelnes Objekt sein."}
            )
            
    if not parsed_json:
        return success_response(data={
            "csv_data": "",
            "converted_count": 0
        })

    # Get all unique keys for header, preserving order of first appearance
    headers = []
    for item in parsed_json:
        if isinstance(item, dict):
            for key in item.keys():
                if key not in headers:
                    headers.append(key)

    if not headers:
        return success_response(data={
            "csv_data": "",
            "converted_count": 0
        })

    output = io.StringIO()
    try:
        writer = csv.DictWriter(output, fieldnames=headers, delimiter=delimiter)
        writer.writeheader()
        
        converted_count = 0
        for item in parsed_json:
            if isinstance(item, dict):
                # Convert complex nested objects to JSON strings instead of stringifying directly?
                # For simplicity, standard stringification for complex types
                row = {}
                for key in headers:
                    if key in item:
                        val = item[key]
                        if isinstance(val, (dict, list)):
                            row[key] = json.dumps(val, ensure_ascii=False)
                        elif val is not None:
                            row[key] = str(val)
                        else:
                            row[key] = ""
                    else:
                        row[key] = ""
                writer.writerow(row)
                converted_count += 1
                
        csv_data = output.getvalue()
    except Exception as e:
        return error_response(
            code=ErrorCodes.INTERNAL_SERVER_ERROR,
            message="Fehler beim Erstellen der CSV-Daten.",
            details={"error": str(e)}
        )
    finally:
        output.close()

    return success_response(data={
        "csv_data": csv_data.strip(),
        "converted_count": converted_count
    })
