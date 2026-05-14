from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.task_breakdown_generator.task_breakdown_generator_validation import validate_task_breakdown_request

api_bp = Blueprint('task_breakdown_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/task_breakdown_generator', methods=['POST'])
def generate_task_breakdown():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_task_breakdown_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    task_text = data.get("task_text", "").strip()
    depth = data.get("depth", 2)
    try:
        depth = int(depth)
    except (ValueError, TypeError):
        depth = 2

    # Break down the task based on depth
    tickets = []
    task_preview = task_text[:25] + "..." if len(task_text) > 25 else task_text
    
    if depth == 1:
        tickets = [
            {"title": f"Phase 1: Implementation of {task_preview}", "description": f"Implement the core logic and components for: {task_text}"},
            {"title": f"Phase 2: Testing & QA for {task_preview}", "description": "Test the implemented features and ensure quality."}
        ]
    elif depth == 2:
        tickets = [
            {"title": f"Setup Environment for {task_preview}", "description": "Prepare the development environment and dependencies."},
            {"title": f"Backend API for {task_preview}", "description": "Implement the necessary backend endpoints and validation."},
            {"title": f"Frontend UI for {task_preview}", "description": "Create the user interface and connect it to the backend."},
            {"title": f"Documentation & Testing for {task_preview}", "description": "Write documentation and add unit tests."}
        ]
    else:
        tickets = [
            {"title": f"Requirements Analysis for {task_preview}", "description": "Analyze the requirements and create a technical specification."},
            {"title": f"Database Schema for {task_preview}", "description": "Design and implement the necessary database migrations."},
            {"title": f"Core Logic for {task_preview}", "description": "Implement the main business logic in the backend."},
            {"title": f"API Endpoint for {task_preview}", "description": "Implement the API routes and response mapping."},
            {"title": f"API Validation for {task_preview}", "description": "Add request validation to all API endpoints."},
            {"title": f"UI Components for {task_preview}", "description": "Create reusable UI components."},
            {"title": f"UI Integration for {task_preview}", "description": "Integrate UI components with the state management and API."},
            {"title": f"Unit Tests for {task_preview}", "description": "Write comprehensive unit tests for all components."},
            {"title": f"E2E Tests for {task_preview}", "description": "Write end-to-end tests for the critical paths."}
        ]

    return success_response(data={
        "tickets": tickets
    })
