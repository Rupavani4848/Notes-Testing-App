from pages.login_page import LoginPage
from pages.notes_page import NotesPage
from config.environment import config
from selenium.webdriver.common.by import By

def test_create_empty_note(driver):

    login = LoginPage(driver)
    notes = NotesPage(driver)

    login.open(config["base_url"])
    login.login(config["user"]["email"], config["user"]["password"])

    notes.click_add_note()

    # click create without entering data
    notes.click(notes.CREATE_BTN)

    title_error = driver.find_element(
        By.XPATH,
        "//*[contains(text(),'Title is required')]"
    )

    desc_error = driver.find_element(
        By.XPATH,
        "//*[contains(text(),'Description is required')]"
    )

    assert title_error.is_displayed()
    assert desc_error.is_displayed()