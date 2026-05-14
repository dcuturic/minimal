from app import create_app
import json

app = create_app()
app.config['TESTING'] = True
client = app.test_client()

data = {
    "text": "helloWorld_this is aTest",
    "target_case": "snakecase"
}

response = client.post('/api/minimal-solutions/case_converter', json=data)
print("Status:", response.status_code)
print("Response:", json.dumps(response.get_json(), indent=2))
