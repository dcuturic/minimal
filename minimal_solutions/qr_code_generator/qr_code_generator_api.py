from flask import Blueprint, request
import io
import base64
try:
    import qrcode
except ImportError:
    qrcode = None

from app.responses import success_response, error_response, ErrorCodes
from .qr_code_generator_validation import validate_qr_code_generator_input

api_bp = Blueprint('qr_code_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/qr_code_generator', methods=['POST'])
def generate_qr_code():
    data = request.get_json(silent=True) or {}
    
    is_valid, errors = validate_qr_code_generator_input(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler.",
            details=errors
        )
        
    if not qrcode:
        return error_response(
            code=ErrorCodes.INTERNAL_SERVER_ERROR,
            message="Die Bibliothek 'qrcode' ist auf dem Server nicht installiert."
        )

    text_content = ""
    qr_type = "text"
    
    if data.get('wifi_ssid'):
        qr_type = "wifi"
        ssid = data.get('wifi_ssid')
        password = data.get('wifi_password', '')
        # Basic WPA wifi format
        text_content = f"WIFI:T:WPA;S:{ssid};P:{password};;"
    elif data.get('url'):
        qr_type = "url"
        text_content = data.get('url')
    elif data.get('text'):
        qr_type = "text"
        text_content = data.get('text')

    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(text_content)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
        
        data_url = f"data:image/png;base64,{img_str}"
        
        return success_response(data={
            "type": qr_type,
            "format": "png",
            "url": data_url
        })
    except Exception as e:
        return error_response(
            code=ErrorCodes.INTERNAL_SERVER_ERROR,
            message="Fehler bei der QR-Code Generierung.",
            details={"exception": str(e)}
        )
