def test_hosting_analyzer_endpoint(client):
    response = client.post(
        '/api/minimal-solutions/hosting_analyzer',
        json={"test": "data"}
    )
    assert response.status_code == 200
