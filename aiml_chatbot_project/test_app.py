import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test that the home page loads correctly"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"AI Chatbot" in response.data

def test_chat_endpoint_basic(client):
    """Test the /chat endpoint with a simple AIML message"""
    response = client.post("/chat", json={"message": "hello"})
    assert response.status_code == 200
    data = response.get_json()
    assert "reply" in data
    assert len(data["reply"]) > 0

def test_chat_weather(client):
    """Test the /chat endpoint with weather query"""
    response = client.post("/chat", json={"message": "weather in Mumbai"})
    assert response.status_code == 200
    data = response.get_json()
    assert "temperature" in data["reply"] or "Sorry" in data["reply"]

def test_chat_wikipedia(client):
    """Test the /chat endpoint with a Wikipedia query"""
    response = client.post("/chat", json={"message": "Who is Albert Einstein?"})
    assert response.status_code == 200
    data = response.get_json()
    assert "Albert Einstein" in data["reply"] or "couldn't find" in data["reply"]
