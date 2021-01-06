import pytest

from app import app

@pytest.fixture
def client():
    return app.test_client()

def do_get(client, path):
    response = client.get(path)
    return response.status_code, str(response.data), response.get_json()

def test_home():
    status_code, body, data = do_get(client, '/')
    old_count = data['count']

    assert status_code == 200
    assert '"text":"Hello, world"' in body
    
    

    for i in range(5):
        status_code, body, data = do_get(client, '/')
        new_count = data['count']

        assert status_code == 200
        assert new_count == old_count + i + 1
 
def test_abuse(client):
    status_code, body, data = do_get(client, '/')
    old_count = data['count']

    assert status_code == 200

    status_code, _, _ = do_get(client, '/abuse')

    assert status_code == 200
    

    status_code, body, data = do_get(client, '/')
    new_count = data['count']

    assert status_code == 200
    assert new_count == old_count +  100 + 1