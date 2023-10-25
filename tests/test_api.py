from datetime import datetime, timedelta, timezone

import httpx
import pytest


@pytest.fixture
def client():
    """
    Not a smart way to do this, as FastAPI provides a TestClient.
    However the point is to access the API running on another process.
    """
    with httpx.Client(base_url="http://localhost:8000") as client:
        yield client


def test_getting_time_endpoint(client):
    response = client.get("/todate/30 days ago")
    assert response.status_code == 200

    msg = response.json()["msg"]
    expected_date = str((datetime.now(tz=timezone.utc) - timedelta(days=30)).date())
    assert msg.startswith(expected_date)


def test_getting_time_endpoint_with_invalid_prompt(client):
    response = client.get("/todate/foobar")
    assert response.status_code == 403
    assert response.json()["detail"] == "Invalid prompt"
