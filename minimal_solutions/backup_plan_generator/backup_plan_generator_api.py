from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.backup_plan_generator.backup_plan_generator_validation import validate_backup_plan_request

api_bp = Blueprint('backup_plan_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/backup_plan_generator', methods=['POST'])
def generate_backup_plan():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_backup_plan_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    frequency = data.get("frequency")
    retention_days = data.get("retention_days")
    storage_type = data.get("storage_type")
    
    # Generate schedule
    schedule = ""
    if frequency == "hourly":
        schedule = "0 * * * *"
    elif frequency == "daily":
        schedule = "0 2 * * *"
    elif frequency == "weekly":
        schedule = "0 3 * * 0"
    elif frequency == "monthly":
        schedule = "0 4 1 * *"
        
    # Generate storage description
    storage_details = ""
    if storage_type == "local":
        storage_details = "Local Storage (/backup) - Fast access, but vulnerable to local hardware failures."
    elif storage_type == "s3":
        storage_details = "AWS S3 - High availability, secure cloud storage."
    elif storage_type == "azure":
        storage_details = "Azure Blob Storage - Enterprise grade cloud storage."
    elif storage_type == "gcs":
        storage_details = "Google Cloud Storage - Scalable and performant object storage."
        
    script_template = f"""#!/bin/bash
# Backup Plan Script Template

# Retention Policy: {retention_days} Days
# Storage Type: {storage_type}
# Cron Schedule: {schedule}

echo "Starting backup process..."

# Your backup commands go here
# e.g., tar -czf backup-$(date +%Y%m%d).tar.gz /data

echo "Backup finished."
"""
    
    plan_data = {
        "schedule": schedule,
        "retention_days": retention_days,
        "storage_details": storage_details,
        "script_template": script_template,
        "frequency": frequency,
        "storage_type": storage_type
    }
    
    return success_response(data=plan_data)
