from pages.login_page import LoginPage
from pages.notes_page import NotesPage
from utils.api_client import APIClient
import time


def test_ui_to_api(driver, config):
    login = LoginPage(driver)
    login.login(config["user"]["email"], config["user"]["password"])

    notes = NotesPage(driver)
    title = "E2E Title"
    desc = "E2E Desc"
    notes.create_note(title, desc)

    # Add a small delay to ensure the note is saved to backend
    time.sleep(1)

    api = APIClient(config["api_url"])
    login_res = api.login(config["user"]["email"], config["user"]["password"])

    token = login_res.json().get("token") or login_res.json().get("data", {}).get("token")

    response = api.get_notes(token)
    
    print("GET NOTES STATUS:", response.status_code)
    print("GET NOTES RESPONSE:", response.text)

    notes_list = response.json()

    # Check if the response contains data field or is directly a list
    if isinstance(notes_list, dict) and "data" in notes_list:
        notes_list = notes_list["data"]

    print("NOTES LIST:", notes_list)
    assert any(title in str(n) for n in notes_list)