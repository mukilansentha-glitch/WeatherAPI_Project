from main import app

def test_homepage():
    tester = app.test_client()
    response = tester.get("/")
    assert response.status_code == 200
