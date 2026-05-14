import re
import colorsys
from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.farbkonverter.farbkonverter_validation import validate_color_request

api_bp = Blueprint('farbkonverter_api', __name__)

def parse_color(val: str):
    val = val.strip().lower()
    
    # 1. HEX
    if val.startswith('#') or re.match(r'^([0-9a-f]{3}|[0-9a-f]{4}|[0-9a-f]{6}|[0-9a-f]{8})$', val):
        if val.startswith('#'):
            hex_val = val[1:]
        else:
            hex_val = val
            
        if len(hex_val) == 3:
            r = int(hex_val[0]*2, 16)
            g = int(hex_val[1]*2, 16)
            b = int(hex_val[2]*2, 16)
            a = 1.0
        elif len(hex_val) == 4:
            r = int(hex_val[0]*2, 16)
            g = int(hex_val[1]*2, 16)
            b = int(hex_val[2]*2, 16)
            a = int(hex_val[3]*2, 16) / 255.0
        elif len(hex_val) == 6:
            r = int(hex_val[0:2], 16)
            g = int(hex_val[2:4], 16)
            b = int(hex_val[4:6], 16)
            a = 1.0
        elif len(hex_val) == 8:
            r = int(hex_val[0:2], 16)
            g = int(hex_val[2:4], 16)
            b = int(hex_val[4:6], 16)
            a = int(hex_val[6:8], 16) / 255.0
        else:
            raise ValueError("Invalid hex length")
        return r, g, b, a
        
    # 2. RGB(A)
    rgb_match = re.match(r'^rgba?\s*\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)(?:\s*,\s*([\d.]+))?\s*\)$', val)
    if rgb_match:
        r = int(rgb_match.group(1))
        g = int(rgb_match.group(2))
        b = int(rgb_match.group(3))
        a = float(rgb_match.group(4)) if rgb_match.group(4) else 1.0
        return r, g, b, a
        
    # 3. HSL(A)
    hsl_match = re.match(r'^hsla?\s*\(\s*([\d.]+)\s*,\s*([\d.]+)%?\s*,\s*([\d.]+)%?(?:\s*,\s*([\d.]+))?\s*\)$', val)
    if hsl_match:
        h = float(hsl_match.group(1)) % 360.0
        s = float(hsl_match.group(2)) / 100.0
        l = float(hsl_match.group(3)) / 100.0
        a = float(hsl_match.group(4)) if hsl_match.group(4) else 1.0
        
        s = max(0.0, min(1.0, s))
        l = max(0.0, min(1.0, l))
        
        r_f, g_f, b_f = colorsys.hls_to_rgb(h / 360.0, l, s)
        return int(round(r_f * 255)), int(round(g_f * 255)), int(round(b_f * 255)), a

    raise ValueError("Unrecognized color format")

def format_hex(r, g, b, a):
    if a == 1.0:
        return f"#{r:02X}{g:02X}{b:02X}"
    else:
        return f"#{r:02X}{g:02X}{b:02X}{int(a*255):02X}"

def format_rgb(r, g, b):
    return f"rgb({r}, {g}, {b})"

def format_rgba(r, g, b, a):
    a_str = f"{a:g}"
    return f"rgba({r}, {g}, {b}, {a_str})"

def format_hsl(r, g, b, a=1.0):
    h_f, l_f, s_f = colorsys.rgb_to_hls(r/255.0, g/255.0, b/255.0)
    h = int(round(h_f * 360.0))
    s = int(round(s_f * 100.0))
    l = int(round(l_f * 100.0))
    if a == 1.0:
        return f"hsl({h}, {s}%, {l}%)"
    else:
        a_str = f"{a:g}"
        return f"hsla({h}, {s}%, {l}%, {a_str})"

@api_bp.route('/api/minimal-solutions/farbkonverter', methods=['POST'])
def handle_farbkonverter():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_color_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    color_value = data.get('color_value')

    try:
        r, g, b, a = parse_color(color_value)
        # Ensure bounds
        r = max(0, min(255, r))
        g = max(0, min(255, g))
        b = max(0, min(255, b))
        a = max(0.0, min(1.0, a))
        
        hex_str = format_hex(r, g, b, a)
        rgb_str = format_rgb(r, g, b)
        rgba_str = format_rgba(r, g, b, a)
        hsl_str = format_hsl(r, g, b, a)
        
        return success_response(data={
            "hex": hex_str,
            "rgb": rgb_str,
            "rgba": rgba_str,
            "hsl": hsl_str
        })
    except ValueError:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Ungültiges Farbformat.",
            details={"color_value": "Bitte geben Sie einen gültigen Farbwert ein (HEX, RGB, RGBA oder HSL)."}
        )
    except Exception:
        return error_response(
            code=ErrorCodes.INTERNAL_SERVER_ERROR,
            message="Interner Fehler beim Verarbeiten der Farbe."
        )
