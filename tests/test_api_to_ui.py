from utils.api_client import APIClient
import time

def test_api_to_ui_sync(driver, config):
    api = APIClient(config["api_url"])

    login_res = api.login(config["user"]["email"], config["user"]["password"])
    token = login_res.json().get("token") or login_res.json().get("data", {}).get("token")

    title = "API Created Note"
    desc = "Created via API"

    api.create_note(token, title, desc)

    driver.refresh()
    
    # Wait for page to reload
    time.sleep(2)

    from pages.login_page import LoginPage
    from pages.notes_page import NotesPage

    login = LoginPage(driver)
    login.login(config["user"]["email"], config["user"]["password"])
    
    # Wait for login to complete and redirect to notes page
    time.sleep(3)

    notes = NotesPage(driver)
    all_notes = notes.get_all_notes()

    assert any(title in note for note in all_notes)