from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.sitemap_xml_generator.sitemap_xml_generator_validation import validate_sitemap_xml_generator_input
import datetime

api_bp = Blueprint('sitemap_xml_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/sitemap_xml_generator', methods=['POST'])
def generate_sitemap_xml():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_sitemap_xml_generator_input(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    urls_input = data.get('urls', '')
    changefreq = data.get('changefreq', '').strip()
    priority = data.get('priority', '')
    
    if isinstance(priority, (int, float)):
        priority = str(priority)
    else:
        priority = priority.strip()

    urls = []
    if isinstance(urls_input, str):
        urls = [url.strip() for url in urls_input.split('\n') if url.strip()]
    elif isinstance(urls_input, list):
        urls = [str(url).strip() for url in urls_input if str(url).strip()]

    lines = []
    lines.append('<?xml version="1.0" encoding="UTF-8"?>')
    lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')

    for url in urls:
        lines.append('  <url>')
        lines.append(f'    <loc>{url}</loc>')
        lines.append(f'    <lastmod>{current_date}</lastmod>')
        if changefreq:
            lines.append(f'    <changefreq>{changefreq}</changefreq>')
        if priority:
            lines.append(f'    <priority>{priority}</priority>')
        lines.append('  </url>')

    lines.append('</urlset>')

    result = "\n".join(lines)

    return success_response(data={
        "result": result
    })
