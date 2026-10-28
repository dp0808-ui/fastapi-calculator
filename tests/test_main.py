from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "FastAPI Calculator App" in response.text

def test_calculate_add():
    response = client.get("/calculate?op=add&a=5&b=3")
    assert response.status_code == 200
    assert response.json()["result"] == 8

def test_calculate_divide_by_zero():
    response = client.get("/calculate?op=divide&a=5&b=0")
    assert response.status_code == 400