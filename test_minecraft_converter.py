from app import create_app

app = create_app()
with app.test_client() as client:
    response = client.post('/api/minimal-solutions/minecraft_converter', json={
        'input_text': 'test block',
        'mode': 'stairs',
        'options': {'variant': 'oak'}
    })
    print('SUCCESS:', response.status_code, response.json)
    
    response = client.post('/api/minimal-solutions/minecraft_converter', json={'mode': 'invalid'})
    print('ERROR:', response.status_code, response.json)
