from app import create_app

def run_tests():
    app = create_app()
    app.testing = True
    client = app.test_client()

    response = client.post('/api/minimal-solutions/knowledge_base_card_generator', json={})
    print('Empty Request:', response.get_json())

    response = client.post('/api/minimal-solutions/knowledge_base_card_generator', json={'source_text': 'a'})
    print('Invalid Length:', response.get_json())

    response = client.post('/api/minimal-solutions/knowledge_base_card_generator', json={'source_text': 'This is a long enough text to test.', 'category': 'General'})
    print('Valid Request:', response.get_json())

if __name__ == "__main__":
    run_tests()
