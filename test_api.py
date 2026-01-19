import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
    """
    Test API health endpoint
    """
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_get_leads_no_params():
    """
    Test getting leads without filters
    """
    response = client.get("/leads")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_leads_with_platform():
    """
    Test filtering leads by platform
    """
    response = client.get("/leads?platform=twitter")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_leads_with_score_filter():
    """
    Test filtering leads by minimum score
    """
    response = client.get("/leads?min_score=70")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_invalid_query_param():
    """
    Test invalid query parameters
    """
    response = client.get("/leads?min_score=invalid")

    assert response.status_code == 422
