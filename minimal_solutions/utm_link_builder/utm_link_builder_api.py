from flask import request
from urllib.parse import urlparse, urlencode, parse_qs, urlunparse

from app.responses import success_response, error_response, ErrorCodes
from .utm_link_builder_validation import validate_utm_link_builder_input

def register_utm_link_builder_api(app):
    @app.route('/api/minimal-solutions/utm_link_builder', methods=['POST'])
    def utm_link_builder_api():
        data = request.get_json(silent=True) or {}
        
        is_valid, errors = validate_utm_link_builder_input(data)
        if not is_valid:
            return error_response(
                code=ErrorCodes.VALIDATION_ERROR,
                message="Validierungsfehler.",
                details=errors
            )
            
        url = data.get('url', '').strip()
        source = data.get('source', '').strip()
        medium = data.get('medium', '').strip()
        campaign = data.get('campaign', '').strip()
        term = data.get('term', '')
        if term:
            term = term.strip()
        content = data.get('content', '')
        if content:
            content = content.strip()
        
        try:
            parsed_url = urlparse(url)
            query_params = parse_qs(parsed_url.query)
            
            # Add UTM parameters
            query_params['utm_source'] = [source]
            query_params['utm_medium'] = [medium]
            query_params['utm_campaign'] = [campaign]
            
            if term:
                query_params['utm_term'] = [term]
            if content:
                query_params['utm_content'] = [content]
                
            new_query = urlencode(query_params, doseq=True)
            
            utm_link = urlunparse((
                parsed_url.scheme,
                parsed_url.netloc,
                parsed_url.path,
                parsed_url.params,
                new_query,
                parsed_url.fragment
            ))
            
            return success_response(data={
                "utm_link": utm_link
            })
        except Exception as e:
            return error_response(
                code=ErrorCodes.INTERNAL_SERVER_ERROR,
                message="Fehler beim Erstellen des UTM Links.",
                details={"exception": str(e)}
            )
