from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.faq_generator.faq_generator_validation import validate_faq_generator_request
import re

api_bp = Blueprint('faq_generator_api', __name__)

def generate_faqs(text, count):
    # Mock behavior based on simple rules or splitting
    sentences = [s.strip() for s in re.split(r'[.!?]', text) if len(s.strip()) > 10]
    faqs = []
    
    # Generic faqs if no sentences could be extracted
    if not sentences:
        faqs.append({
            "question": "What is this text about?",
            "answer": "The provided text does not contain enough information to generate specific FAQs."
        })
        return faqs[:count]

    for i, sentence in enumerate(sentences):
        if len(faqs) >= count:
            break
        
        words = sentence.split()
        if len(words) < 3:
            continue
            
        topic = " ".join(words[:3])
        question = f"What is the significance of {topic}?"
        answer = f"According to the source: {sentence}."
        
        faqs.append({
            "question": question,
            "answer": answer
        })

    # Fill up if we don't have enough
    default_questions = [
        ("Can you summarize the main point?", "The text focuses on the core concepts mentioned in the source material."),
        ("Who might find this useful?", "Anyone interested in the primary topics discussed in the text."),
        ("What are the key takeaways?", "The key takeaways are the central arguments and details outlined in the text.")
    ]
    
    idx = 0
    while len(faqs) < count and idx < len(default_questions):
        faqs.append({
            "question": default_questions[idx][0],
            "answer": default_questions[idx][1]
        })
        idx += 1
        
    return faqs

@api_bp.route('/api/minimal-solutions/faq_generator', methods=['POST'])
def handle_faq_generator():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_faq_generator_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )
        
    source_text = data.get('source_text', '')
    count = data.get('count', 3)
    if count is not None:
        count = int(count)
    else:
        count = 3
    
    try:
        faqs = generate_faqs(source_text, count)
    except Exception as e:
        return error_response(
            code=ErrorCodes.INTERNAL_SERVER_ERROR,
            message="Interner Fehler beim Erstellen der FAQs."
        )
        
    return success_response(data={"faqs": faqs})
