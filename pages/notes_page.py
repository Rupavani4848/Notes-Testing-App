from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage


class NotesPage(BasePage):

    ADD_BTN = (By.XPATH, "//button[contains(text(),'Add')]")
    TITLE = (By.ID, "title")
    DESC = (By.ID, "description")
    SAVE_BTN = (By.XPATH, "//button[text()='Create']")
    CREATE_BTN = SAVE_BTN

    def click_add_note(self):
        self.click(self.ADD_BTN)

    def create_note(self, title, desc, open_form=True):
        if open_form:
            self.click(self.ADD_BTN)

        # Wait for the form to appear
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.TITLE)
        )
        self.send_keys(self.TITLE, title)
        self.send_keys(self.DESC, desc)
        self.click(self.SAVE_BTN)

        # Wait for the modal to close
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(self.TITLE)
        )

        if title:
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(
                    (By.XPATH, f"//*[contains(text(), '{title}')]")
                )
            )

    def delete_note(self, title):
        note_locator = (By.XPATH, f"//*[contains(text(), '{title}')]")
        note_element = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(note_locator)
        )

        delete_locator = (By.XPATH,
            f"//*[contains(text(), '{title}')]/ancestor::div[1]//button[contains(translate(normalize-space(.), 'DELETE', 'delete'), 'delete') or contains(@aria-label, 'Delete') or contains(@title, 'Delete')]"
        )
        try:
            self.click(delete_locator)
        except Exception:
            delete_locator_alt = (By.XPATH,
                f"//*[contains(text(), '{title}')]/following::button[contains(translate(normalize-space(.), 'DELETE', 'delete'), 'delete')][1]"
            )
            self.click(delete_locator_alt)

        # Handle confirmation popup
        confirm_locator = (By.XPATH, "//button[contains(text(),'Yes') or contains(text(),'Delete') or contains(text(),'Confirm') or contains(@class,'btn-danger') or contains(@class,'confirm')]")
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(confirm_locator))
            self.click(confirm_locator)
        except Exception:
            pass  # No confirmation popup

        WebDriverWait(self.driver, 15).until(
            EC.invisibility_of_element_located(note_locator)
        )

    def get_all_notes(self):
        # Wait for the notes container to be visible (indicates page fully loaded)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//div[contains(@class,'notes-container') or contains(@class,'notes-list') or contains(@class,'card-body') or contains(@class,'note-items')]")
                )
            )
        except TimeoutException:
            pass  # Container might not have this class

        # Wait for at least one note card to be present
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//div[contains(@class,'card') or contains(@class,'note') or contains(@class,'note-item') or contains(@class,'list-group-item')]")
            )
        )
        
        # Extract text from all note elements
        elements = self.driver.find_elements(
            By.XPATH,
            "//div[contains(@class,'card') or contains(@class,'note') or contains(@class,'note-item') or contains(@class,'list-group-item')]//h5 | //div[contains(@class,'card') or contains(@class,'note') or contains(@class,'note-item') or contains(@class,'list-group-item')]//h6 | //div[contains(@class,'card') or contains(@class,'note') or contains(@class,'note-item') or contains(@class,'list-group-item')]"
        )
        
        # Filter and collect text, handling empty elements
        notes_list = []
        for element in elements:
            text = element.text.strip()
            if text and len(text) > 0:
                notes_list.append(text)
        
        return notes_list if notes_list else []

    def is_note_present(self, title):
        locator = (By.XPATH, f"//*[contains(text(), '{title}')]")
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False