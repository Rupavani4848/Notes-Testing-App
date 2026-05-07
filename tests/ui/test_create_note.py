from pages.login_page import LoginPage
from pages.notes_page import NotesPage

def test_create_note(driver, config):
    login = LoginPage(driver)
    login.login(config["user"]["email"], config["user"]["password"])

    notes = NotesPage(driver)
    notes.create_note("Test Title", "Test Description")

    assert len(notes.get_all_notes()) > 0