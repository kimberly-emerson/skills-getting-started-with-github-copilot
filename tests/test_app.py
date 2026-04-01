
import pytest
from fastapi.testclient import TestClient
from src.app import app, activities

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_activity():
    # Use a real activity from the app's in-memory database
    activity = "Chess Club"
    email = "testuser@mergington.edu"
    # Remove test user if already present (idempotent for repeated test runs)
    if email in activities[activity]["participants"]:
        activities[activity]["participants"].remove(email)
    response = client.post(f"/activities/{activity}/signup?email={email}")
    # Accept 200 (success) or 400 (already signed up)
    assert response.status_code in (200, 400)
