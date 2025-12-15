import requests
import pytest


BASE_URL = "https://reqres.in"


def test_get_single_user_success():
    response = requests.get(f"{BASE_URL}/api/users/2")

    assert response.status_code == 200
    data = response.json()

    assert data.get("data", {}).get("id") == 2
    assert "@reqres.in" in data.get("data", {}).get("email", "")


def test_create_user():
    payload = {"name": "Raisa", "job": "qa_tester"}
    response = requests.post(f"{BASE_URL}/api/users", json=payload)

    assert response.status_code == 201
    data = response.json()

    assert data.get("name") == payload["name"]
    assert data.get("job") == payload["job"]
    assert "id" in data
    assert "createdAt" in data


def test_get_non_existing_user():
    response = requests.get(f"{BASE_URL}/api/users/23")

    assert response.status_code == 404
    assert response.text == "{}"

