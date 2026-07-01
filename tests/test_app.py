from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant_removes_participant_from_activity():
    response = client.delete(
        "/activities/Chess%20Club/participants/michael@mergington.edu"
    )

    assert response.status_code == 200
    assert "michael@mergington.edu" in response.json()["message"]

    activities_response = client.get("/activities")
    activity = activities_response.json()["Chess Club"]
    assert "michael@mergington.edu" not in activity["participants"]
