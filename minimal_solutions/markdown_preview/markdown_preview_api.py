from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.markdown_preview.markdown_preview_validation import validate_input
import html
import re

api_bp = Blueprint('markdown_preview_api', __name__)

def basic_markdown_to_html(md_text):
    try:
        import markdown
        return markdown.markdown(md_text, extensions=['fenced_code', 'tables'])
    except ImportError:
        pass
        
    # Fallback basic Markdown parsing if the library is not available
    # Escape HTML first
    text = html.escape(md_text)
    
    # Headers
    text = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    text = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    text = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', text, flags=re.MULTILINE)
    
    # Bold
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    # Italic
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    
    # Code blocks
    def repl_code_block(m):
        code_content = m.group(1).strip()
        return f"<pre><code>{code_content}</code></pre>"
    text = re.sub(r'```(?:\w+)?\n(.*?)```', repl_code_block, text, flags=re.DOTALL)
    
    # Inline code
    text = re.sub(r'`(.*?)`', r'<code>\1</code>', text)
    
    # Lists (very basic)
    text = re.sub(r'^- (.*?)$', r'<li>\1</li>', text, flags=re.MULTILINE)
    text = re.sub(r'(<li>.*?</li>\n?)+', lambda m: f"<ul>\n{m.group(0)}</ul>\n", text)
    
    # Links
    text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', text)
    
    # Paragraphs (basic implementation: double newline to paragraph)
    paragraphs = text.split('\n\n')
    html_paragraphs = []
    for p in paragraphs:
        p = p.strip()
        if p and not p.startswith('<h') and not p.startswith('<pre') and not p.startswith('<ul'):
            p = '<p>' + p.replace('\n', '<br>') + '</p>'
        if p:
            html_paragraphs.append(p)
        
    return '\n'.join(html_paragraphs)

@api_bp.route('/api/minimal-solutions/markdown_preview', methods=['POST'])
def markdown_preview():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt."
        )

    is_valid, errors = validate_input(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    markdown_text = data['markdown_text']

    try:
        html_result = basic_markdown_to_html(markdown_text)
        return success_response(data={
            "html": html_result,
            "original_length": len(markdown_text)
        })
    except Exception as e:
        return error_response(
            code=ErrorCodes.INTERNAL_ERROR,
            message="Ein unerwarteter Fehler ist aufgetreten.",
            details={"error": str(e)}
        )
