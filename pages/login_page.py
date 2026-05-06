from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class LoginPage(BasePage):

    LOGIN_NAV_BTN = (By.XPATH, "//a[text()='Login']")
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.XPATH, "//button[text()='Login']")
    ERROR_MSG = (
        By.XPATH,
        "//div[contains(@class,'alert') or contains(@class,'toast') or contains(@class,'notification') or contains(@class,'invalid-feedback') or contains(text(),'Incorrect email address or password') or contains(text(),'Invalid') or contains(text(),'invalid') or contains(text(),'incorrect') or contains(text(),'required')]"
    )

    def login(self, email, password):
        try:
            self.click(self.LOGIN_NAV_BTN)
        except Exception:
            pass

        self.send_keys(self.EMAIL, email)
        self.send_keys(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def get_error_message(self):
        # First try to find auth error (alert/toast/notification)
        try:
            auth_error = WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,'alert') or contains(@class,'toast') or contains(@class,'notification')]"))
            )
            if auth_error.text and auth_error.text.strip():
                return auth_error.text.strip()
        except:
            pass

        # Wait for at least one invalid-feedback element with text
        try:
            WebDriverWait(self.driver, 10).until(
                lambda d: any(
                    elem.is_displayed() and elem.text.strip()
                    for elem in d.find_elements(By.CSS_SELECTOR, ".invalid-feedback")
                )
            )
            # Now find the first visible one with text
            field_errors = self.driver.find_elements(By.CSS_SELECTOR, ".invalid-feedback")
            for error in field_errors:
                if error.is_displayed() and error.text.strip():
                    return error.text.strip()
        except:
            pass

        # Last resort: look for any visible error element
        try:
            error = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, "//*[contains(@class,'invalid-feedback') or contains(@class,'alert') or contains(@class,'error')]"))
            )
            if error.text.strip():
                return error.text.strip()
        except:
            raise Exception("No error message found on the page")