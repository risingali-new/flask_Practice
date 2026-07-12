import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_add_page():
    client = app.test_client()
    response = client.get("/add")
    assert response.status_code == 200


def test_app_exists():
    assert app is not None


def test_secret_key():
    assert app.secret_key is not None