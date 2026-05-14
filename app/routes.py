from flask import Blueprint, render_template, request
from .registry import registry
from .responses import success_response, error_response, ErrorCodes
from datetime import datetime, timezone

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/minimal-solutions')
def solutions_overview():
    solutions = registry.get_all()
    categories = {}
    for sol in solutions:
        cat = sol.get('category', 'Uncategorized')
        categories[cat] = categories.get(cat, 0) + 1
    total_count = len(solutions)
    return render_template('overview.html', solutions=solutions, categories=categories, total_count=total_count)

@main.route('/minimal-solutions/<identify>')
def solution_detail(identify):
    solution = registry.get(identify)
    if not solution:
        return render_template('404.html', message=f"Solution '{identify}' not found."), 404
    return render_template('detail.html', identify=identify, solution=solution)

@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html', message="The requested page was not found."), 404

# API Standard base
@main.route('/api/minimal-solutions')
def api_solutions_overview():
    return success_response(data={"solutions": registry.get_all()})

@main.route('/api/minimal-solutions/search')
def api_solutions_search():
    query = request.args.get('q', '')
    results = registry.search(query)
    return success_response(data={"solutions": results, "count": len(results)})

@main.route('/api/minimal-solutions/export')
def api_solutions_export():
    solutions = registry.get_all()
    public_solutions = []
    for sol in solutions:
        public_sol = {
            "identify": sol.get("identify"),
            "title": sol.get("title"),
            "category": sol.get("category"),
            "description": sol.get("description"),
            "tags": sol.get("tags"),
            "ui_route": sol.get("ui_route"),
            "api_endpoint": sol.get("api_endpoint"),
            "status": sol.get("status")
            # 'folder' is excluded to hide internal structure (secrets)
        }
        public_solutions.append(public_sol)
        
    meta = {
        "version": "1.0",
        "exported_at": datetime.now(timezone.utc).isoformat(),
        "total_solutions": len(public_solutions)
    }
    
    return success_response(data={"solutions": public_solutions}, meta=meta)
