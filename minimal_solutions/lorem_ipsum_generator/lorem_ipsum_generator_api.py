from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.lorem_ipsum_generator.lorem_ipsum_generator_validation import validate_lorem_ipsum_generator_request
import random

api_bp = Blueprint('lorem_ipsum_generator_api', __name__)

LOREM_WORDS = [
    "lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit",
    "sed", "do", "eiusmod", "tempor", "incididunt", "ut", "labore", "et", "dolore",
    "magna", "aliqua", "ut", "enim", "ad", "minim", "veniam", "quis", "nostrud",
    "exercitation", "ullamco", "laboris", "nisi", "ut", "aliquip", "ex", "ea",
    "commodo", "consequat", "duis", "aute", "irure", "dolor", "in", "reprehenderit",
    "in", "voluptate", "velit", "esse", "cillum", "dolore", "eu", "fugiat", "nulla",
    "pariatur", "excepteur", "sint", "occaecat", "cupidatat", "non", "proident",
    "sunt", "in", "culpa", "qui", "officia", "deserunt", "mollit", "anim", "id", "est", "laborum"
]

def generate_words(count: int) -> str:
    if count == 0:
        return ""
    words = []
    for i in range(count):
        word = random.choice(LOREM_WORDS)
        if i == 0:
            word = word.capitalize()
        words.append(word)
    
    result = " ".join(words)
    if result:
        result += "."
    return result

def generate_sentences(count: int) -> str:
    sentences = []
    for _ in range(count):
        word_count = random.randint(5, 15)
        sentences.append(generate_words(word_count))
    return " ".join(sentences)

def generate_paragraphs(count: int) -> str:
    paragraphs = []
    for _ in range(count):
        sentence_count = random.randint(3, 7)
        paragraphs.append(generate_sentences(sentence_count))
    return "\n\n".join(paragraphs)

def generate_bytes(count: int) -> str:
    text = ""
    while len(text.encode('utf-8')) < count:
        text += random.choice(LOREM_WORDS) + " "
    
    text = text.strip()
    byte_str = text.encode('utf-8')
    if len(byte_str) > count:
        byte_str = byte_str[:count]
    return byte_str.decode('utf-8', errors='ignore')

def generate_lists(count: int) -> str:
    items = []
    for _ in range(count):
        word_count = random.randint(3, 8)
        items.append(f"- {generate_words(word_count)}")
    return "\n".join(items)

@api_bp.route('/api/minimal-solutions/lorem_ipsum_generator', methods=['POST'])
def handle_lorem_ipsum_generator():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_lorem_ipsum_generator_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    mode = data['mode']
    count = data['count']
    
    text = ""
    if mode == 'words':
        text = generate_words(count)
    elif mode == 'paragraphs':
        text = generate_paragraphs(count)
    elif mode == 'bytes':
        text = generate_bytes(count)
    elif mode == 'lists':
        text = generate_lists(count)

    return success_response(data={
        "text": text
    })
