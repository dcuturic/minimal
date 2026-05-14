from app import create_app

app = create_app()
with app.test_client() as client:
    response = client.post('/api/minimal-solutions/datumsdifferenz_rechner', json={'start_date': '2023-01-01', 'end_date': '2024-02-15'})
    print('SUCCESS:', response.status_code, response.json)
    
    response = client.post('/api/minimal-solutions/datumsdifferenz_rechner', json={'start_date': 'invalid', 'end_date': '2024-02-15'})
    print('ERROR:', response.status_code, response.json)
