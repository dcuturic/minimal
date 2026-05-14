from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.cron_expression_helper.cron_expression_helper_validation import validate_cron_request
from datetime import datetime, timedelta

api_bp = Blueprint('cron_expression_helper_api', __name__)

def parse_cron_part(part, min_val, max_val):
    if part == '*':
        return set(range(min_val, max_val + 1))
    if part.startswith('*/'):
        try:
            step = int(part[2:])
            if step > 0:
                return set(range(min_val, max_val + 1, step))
        except ValueError:
            return set()
    
    values = set()
    for item in part.split(','):
        if '-' in item:
            try:
                start, end = map(int, item.split('-'))
                values.update(range(start, end + 1))
            except ValueError:
                pass
        else:
            try:
                values.add(int(item))
            except ValueError:
                pass
    return {v for v in values if min_val <= v <= max_val}

def get_next_executions(cron_expression, count=5):
    parts = cron_expression.strip().split()
    if len(parts) != 5:
        return []
    
    minutes = parse_cron_part(parts[0], 0, 59)
    hours = parse_cron_part(parts[1], 0, 23)
    days = parse_cron_part(parts[2], 1, 31)
    months = parse_cron_part(parts[3], 1, 12)
    
    dow_parsed = parse_cron_part(parts[4], 0, 7)
    dow = set()
    for d in dow_parsed:
        if d == 7:
            dow.add(0)
        else:
            dow.add(d)
            
    if not all([minutes, hours, days, months, dow]):
        return []

    now = datetime.now()
    current = now.replace(second=0, microsecond=0) + timedelta(minutes=1)
    
    executions = []
    attempts = 0
    while len(executions) < count and attempts < 100000:
        attempts += 1
        
        if current.month not in months:
            try:
                next_month = current.replace(day=28) + timedelta(days=4)
                current = next_month.replace(day=1, hour=0, minute=0)
            except Exception:
                current += timedelta(days=30)
            continue
            
        py_to_cron_dow = (current.weekday() + 1) % 7
        
        is_dom_restricted = parts[2] != '*'
        is_dow_restricted = parts[4] != '*'
        
        if is_dom_restricted and is_dow_restricted:
            day_match = (current.day in days) or (py_to_cron_dow in dow)
        else:
            day_match = (current.day in days) and (py_to_cron_dow in dow)
            
        if not day_match:
            current += timedelta(days=1)
            current = current.replace(hour=0, minute=0)
            continue
            
        if current.hour not in hours:
            current += timedelta(hours=1)
            current = current.replace(minute=0)
            continue
            
        if current.minute not in minutes:
            current += timedelta(minutes=1)
            continue
            
        executions.append(current.strftime("%Y-%m-%d %H:%M:00"))
        current += timedelta(minutes=1)
        
    return executions

def describe_cron(cron_expression):
    parts = cron_expression.strip().split()
    if len(parts) != 5:
        return "Ungültiger Cron-Ausdruck"
        
    minute, hour, day, month, dow = parts
    desc = []
    
    if minute == '*' and hour == '*':
        desc.append("Jede Minute")
    elif minute.startswith('*/'):
        desc.append(f"Alle {minute[2:]} Minuten")
    elif minute != '*' and hour == '*':
        desc.append(f"Jede Stunde zur Minute {minute}")
    elif minute != '*' and hour != '*':
        if hour.startswith('*/'):
            desc.append(f"Alle {hour[2:]} Stunden zur Minute {minute}")
        else:
            desc.append(f"Täglich um {hour.zfill(2)}:{minute.zfill(2)} Uhr")
    else:
        desc.append("Zu spezifischen Zeiten")
        
    if day != '*':
        desc.append(f"am {day}. des Monats")
    if month != '*':
        desc.append(f"im Monat {month}")
    if dow != '*':
        dow_map = {'0': 'Sonntag', '1': 'Montag', '2': 'Dienstag', '3': 'Mittwoch', '4': 'Donnerstag', '5': 'Freitag', '6': 'Samstag', '7': 'Sonntag'}
        if dow in dow_map:
            desc.append(f"und nur am {dow_map[dow]}")
        else:
            desc.append(f"an den Wochentagen {dow}")
            
    return " ".join(desc)

@api_bp.route('/api/minimal-solutions/cron_expression_helper', methods=['POST'])
def handle_cron_helper():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_cron_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    cron_expression = data.get('cron_expression')
    
    next_executions = get_next_executions(cron_expression, 5)
    description = describe_cron(cron_expression)
    
    if not next_executions:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Der Cron-Ausdruck konnte nicht ausgewertet werden oder führt zu keinen Ausführungen in absehbarer Zeit."
        )

    return success_response(data={
        "expression": cron_expression,
        "description": description,
        "next_executions": next_executions
    })
