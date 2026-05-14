from flask import Blueprint, request
from .hashtag_generator_validation import validate_request
from app.responses import success_response, error_response, ErrorCodes

api_bp = Blueprint('hashtag_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/hashtag_generator', methods=['POST'])
def generate():
    data = request.get_json() or {}
    
    is_valid, errors = validate_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors,
            status_code=400
        )
    
    topic = data.get('topic', '').strip()
    audience = data.get('audience', '').strip()
    count = int(data.get('count', 10))
    
    topic_clean = "".join([c for c in topic if c.isalnum()])
    audience_clean = "".join([c for c in audience if c.isalnum()])
    
    base_hashtags = []
    if topic_clean:
        base_hashtags.extend([f"#{topic_clean}", f"#{topic_clean}Life", f"#{topic_clean}Tips", f"#{topic_clean}Community", f"#{topic_clean}Vibes"])
    
    if audience_clean:
        base_hashtags.extend([f"#{audience_clean}", f"#{audience_clean}Love", f"#{audience_clean}Goals", f"#{audience_clean}Style", f"#{audience_clean}Network"])
        if topic_clean:
            base_hashtags.append(f"#{topic_clean}For{audience_clean}")

    base_hashtags.extend(["#trending", "#viral", "#instagood", "#explorepage", "#fyp", "#foryou", "#explore", "#inspiration"])
    
    hashtags = []
    seen = set()
    for ht in base_hashtags:
        if ht and ht not in seen and ht != "#":
            seen.add(ht)
            hashtags.append(ht)
            
    i = 1
    while len(hashtags) < count:
        if topic_clean:
            ht = f"#{topic_clean}{i}"
        else:
            ht = f"#hashtag{i}"
        if ht not in seen:
            seen.add(ht)
            hashtags.append(ht)
        i += 1
        
    hashtags = hashtags[:count]
    result_text = " ".join(hashtags)
    
    return success_response({
        "hashtags": result_text,
        "list": hashtags
    })
