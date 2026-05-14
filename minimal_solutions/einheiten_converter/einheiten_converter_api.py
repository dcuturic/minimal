from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.einheiten_converter.einheiten_converter_validation import validate_einheiten_converter_input

api_bp = Blueprint('einheiten_converter_api', __name__)

CONVERSIONS = {
    "length": {
        "base": "m",
        "multipliers": {
            "mm": 0.001,
            "cm": 0.01,
            "m": 1.0,
            "km": 1000.0,
            "in": 0.0254,
            "ft": 0.3048,
            "yd": 0.9144,
            "mi": 1609.344
        }
    },
    "weight": {
        "base": "kg",
        "multipliers": {
            "mg": 0.000001,
            "g": 0.001,
            "kg": 1.0,
            "t": 1000.0,
            "oz": 0.0283495,
            "lb": 0.453592
        }
    },
    "speed": {
        "base": "m/s",
        "multipliers": {
            "m/s": 1.0,
            "km/h": 0.277778,
            "mph": 0.44704,
            "kn": 0.514444
        }
    },
    "volume": {
        "base": "l",
        "multipliers": {
            "ml": 0.001,
            "l": 1.0,
            "gal": 3.78541,
            "qt": 0.946353,
            "pt": 0.473176,
            "cup": 0.236588
        }
    },
    "area": {
        "base": "sq_m",
        "multipliers": {
            "sq_m": 1.0,
            "sq_km": 1000000.0,
            "sq_ft": 0.092903,
            "sq_yd": 0.836127,
            "sq_mi": 2589988.11,
            "ac": 4046.86,
            "ha": 10000.0
        }
    }
}

def convert_unit(value, from_unit, to_unit, category):
    value = float(value)
    
    # Handle temperature specially since it's not a simple multiplier
    if category == "temperature":
        # Convert to Kelvin first
        if from_unit == "c":
            k = value + 273.15
        elif from_unit == "f":
            k = (value - 32) * 5/9 + 273.15
        elif from_unit == "k":
            k = value
        else:
            raise ValueError(f"Unbekannte Temperatureinheit: {from_unit}")
            
        # Convert from Kelvin to target
        if to_unit == "c":
            return k - 273.15
        elif to_unit == "f":
            return (k - 273.15) * 9/5 + 32
        elif to_unit == "k":
            return k
        else:
            raise ValueError(f"Unbekannte Temperatureinheit: {to_unit}")
            
    if category in CONVERSIONS:
        cat_data = CONVERSIONS[category]
        if from_unit not in cat_data["multipliers"] or to_unit not in cat_data["multipliers"]:
            raise ValueError(f"Unbekannte Einheit für Kategorie {category}")
        
        base_value = value * cat_data["multipliers"][from_unit]
        target_value = base_value / cat_data["multipliers"][to_unit]
        return target_value
        
    raise ValueError(f"Unbekannte Kategorie: {category}")

@api_bp.route('/api/minimal-solutions/einheiten_converter', methods=['POST'])
def handle_einheiten_converter():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_einheiten_converter_input(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    value = data.get('value')
    from_unit = data.get('from_unit')
    to_unit = data.get('to_unit')
    category = data.get('category')
    
    try:
        result = convert_unit(value, from_unit, to_unit, category)
    except ValueError as e:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message=str(e)
        )
    except Exception:
        return error_response(
            code=ErrorCodes.INTERNAL_SERVER_ERROR,
            message="Interner Fehler bei der Konvertierung."
        )

    return success_response(data={
        "result": result
    })
