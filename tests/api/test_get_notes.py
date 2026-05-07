import json

import pytest

try:
    import allure
except ImportError:
    allure = None

from utils.api_client import APIClient


def test_get_all_notes_from_api_and_report(config):
    api = APIClient(config["api_url"])

    login_response = api.login(config["user"]["email"], config["user"]["password"])
    assert login_response.status_code == 200, f"Login failed: {login_response.text}"

    token = login_response.json().get("token") or login_response.json().get("data", {}).get("token")
    assert token, "Failed to retrieve auth token from login response"

    response = api.get_notes(token)
    assert response.status_code == 200, f"Get notes failed: {response.text}"

    notes_payload = response.json()
    if isinstance(notes_payload, dict) and "data" in notes_payload:
        notes_list = notes_payload["data"]
    elif isinstance(notes_payload, list):
        notes_list = notes_payload
    else:
        raise AssertionError(f"Unexpected notes response format: {notes_payload}")

    assert isinstance(notes_list, list), "Notes response is not a list"
    assert notes_list, "No notes were returned by the API"

    note_lines = []
    for note in notes_list:
        title = note.get("title") or note.get("name") or "<no title>"
        description = note.get("description") or note.get("desc") or "<no description>"
        note_lines.append(f"Title: {title}\nDescription: {description}")

    notes_text = "\n\n".join(note_lines)

    if allure:
        allure.attach(
            notes_text,
            name="All Notes from API",
            attachment_type=allure.attachment_type.TEXT,
        )
        allure.attach(
            json.dumps(notes_list, indent=2),
            name="All Notes JSON",
            attachment_type=allure.attachment_type.JSON,
        )

    print("Retrieved notes count:", len(notes_list))
    print(notes_text)
