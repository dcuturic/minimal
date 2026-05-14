from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.random_name_generator.random_name_generator_validation import validate_random_name_generator_request
import random

api_bp = Blueprint('random_name_generator_api', __name__)

NAMES = {
    'project': ['NexusCore', 'QuantumSync', 'AeroShift', 'TechVibe', 'InnovateX', 'SynergyLabs', 'ElevateHQ', 'VentureStack', 'PioneerDynamics', 'ApexSolutions'],
    'server': ['alpha-node-01', 'omega-proxy', 'db-cluster-eu', 'cache-redis-main', 'worker-queue-5', 'bastion-host', 'loadbalancer-ext', 'auth-service', 'metrics-agent', 'storage-nas-2'],
    'bot': ['AutoResponder9000', 'ChatHelper', 'DataScraperBot', 'TaskAutomator', 'SupportDroid', 'CryptoTraderBot', 'ModerationAI', 'ReminderBot', 'WeatherBot', 'PingMonitor'],
    'fantasy': ['Aelrindel', 'Faenor', 'Olorin', 'Galadriel', 'Thorin', 'Eldarion', 'Luthien', 'Gimli', 'Aragorn', 'Legolas', 'Eowyn', 'Faramir', 'Elrond', 'Arwen', 'Thranduil'],
    'scifi': ['Zark', 'Xylan', 'Nova', 'Orion', 'Cygnus', 'Lyra', 'Cassiopeia', 'Rigel', 'Vega', 'Altair', 'Drax', 'Groot', 'Korben', 'Leeloo', 'Neo'],
    'nature': ['Oak', 'Willow', 'River', 'Mountain', 'Breeze', 'Stone', 'Leaf', 'Forest', 'Stream', 'Meadow', 'Sky', 'Cloud', 'Sunrise', 'Ocean', 'Valley']
}

@api_bp.route('/api/minimal-solutions/random_name_generator', methods=['POST'])
def handle_random_name_generator():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_random_name_generator_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    category = data['category']
    count = data['count']
    
    category_names = NAMES.get(category, NAMES['project'])
    
    result = []
    for _ in range(count):
        result.append(random.choice(category_names))

    return success_response(data={
        "names": result
    })
