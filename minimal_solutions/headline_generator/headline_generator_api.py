from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.headline_generator.headline_generator_validation import validate_headline_request
import random

api_bp = Blueprint('headline_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/headline_generator', methods=['POST'])
def handle_headline_generator():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_headline_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    topic = data.get('topic', '').strip()
    style = data.get('style', '').strip()
    count_val = data.get('count')
    
    try:
        count = int(count_val) if count_val is not None else 3
    except (ValueError, TypeError):
        count = 3

    # Templates
    templates = {
        "professional": [
            "The Ultimate Guide to {topic}",
            "Why {topic} is Essential for Success",
            "Best Practices for {topic} in 2024",
            "How to Master {topic}",
            "The Future of {topic}: Trends and Insights",
            "A Comprehensive Overview of {topic}",
            "Key Strategies for Implementing {topic}",
            "Top 5 Things You Must Know About {topic}",
            "The Definitive Playbook for {topic}",
            "How {topic} is Transforming the Industry"
        ],
        "creative": [
            "Unlock the Magic of {topic}",
            "5 Unexpected Ways {topic} Will Change Your Life",
            "The Secret Art of {topic} Revealed",
            "Diving Deep into the World of {topic}",
            "How {topic} Sparked a Revolution",
            "Everything You Never Knew About {topic}",
            "The {topic} Renaissance is Here",
            "Breaking Boundaries with {topic}",
            "A Fresh Perspective on {topic}",
            "The Hidden Genius of {topic}"
        ],
        "clickbait": [
            "You Won't Believe This Trick for {topic}!",
            "10 {topic} Secrets the Experts Don't Want You to Know",
            "They Laughed When I Tried {topic}, But Then...",
            "The Shocking Truth About {topic}",
            "Is {topic} a Scam? We Investigated!",
            "Do This One Thing to Fix Your {topic} Now",
            "Stop Doing {topic} Like This Immediately!",
            "The Most Controversial Opinion on {topic}",
            "This {topic} Hack Will Blow Your Mind!",
            "Why Everyone is Obsessed with {topic}"
        ],
        "educational": [
            "Understanding {topic}: A Step-by-Step Tutorial",
            "The Science Behind {topic} Explained",
            "{topic} 101: Everything You Need to Know",
            "A Beginner's Guide to Exploring {topic}",
            "How Does {topic} Actually Work?",
            "The History and Evolution of {topic}",
            "Learning {topic} From Scratch",
            "Common Misconceptions About {topic}",
            "An In-Depth Look at {topic}",
            "Mastering the Basics of {topic}"
        ]
    }

    style_key = style.lower()
    selected_templates = templates.get(style_key, templates["professional"])
    
    random.shuffle(selected_templates)
    chosen = selected_templates[:count]
    
    headlines = [t.format(topic=topic) for t in chosen]
    
    while len(headlines) < count:
        headlines.append(random.choice(selected_templates).format(topic=topic))

    return success_response(data={
        "headlines": headlines
    })
