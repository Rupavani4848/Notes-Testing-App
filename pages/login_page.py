from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from utils.logger import logger


class LoginPage(BasePage):

    LOGIN_NAV_BTN = [
        (By.XPATH, "//a[text()='Login']"),
        (By.PARTIAL_LINK_TEXT, "Login")
    ]

    EMAIL = [
        (By.ID, "email"),
        (By.NAME, "email"),
        (By.XPATH, "//input[@type='email']")
    ]

    PASSWORD = [
        (By.ID, "password"),
        (By.NAME, "password"),
        (By.XPATH, "//input[@type='password']")
    ]

    LOGIN_BTN = [
        (By.XPATH, "//button[text()='Login']"),
        (By.CSS_SELECTOR, "button[type='submit']")
    ]

    ERROR_MSG = (
        By.XPATH,
        "//div[contains(@class,'alert') or "
        "contains(@class,'toast') or "
        "contains(@class,'notification') or "
        "contains(@class,'invalid-feedback') or "
        "contains(text(),'Incorrect email address or password') or "
        "contains(text(),'Invalid') or "
        "contains(text(),'invalid') or "
        "contains(text(),'incorrect') or "
        "contains(text(),'required')]"
    )

    def login(self, email, password):

        logger.info("Starting login process")

        try:

            self.click(self.LOGIN_NAV_BTN)

        except Exception:

            logger.warning(
                "Login navigation button not available"
            )

        self.send_keys(self.EMAIL, email)

        self.send_keys(self.PASSWORD, password)

        self.click(self.LOGIN_BTN)

        logger.info("Login action completed")

    def get_error_message(self):

        logger.info("Fetching login error message")

        # Alert / Toast / Notification messages
        try:

            auth_error = WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        "//div[contains(@class,'alert') or "
                        "contains(@class,'toast') or "
                        "contains(@class,'notification')]"
                    )
                )
            )

            if auth_error.text and auth_error.text.strip():

                logger.info(
                    f"Auth error found: {auth_error.text}"
                )

                return auth_error.text.strip()

        except Exception:

            logger.warning(
                "No auth alert/toast message found"
            )

        # Field validation messages
        try:

            WebDriverWait(self.driver, 10).until(
                lambda d: any(
                    elem.is_displayed() and elem.text.strip()
                    for elem in d.find_elements(
                        By.CSS_SELECTOR,
                        ".invalid-feedback"
                    )
                )
            )

            field_errors = self.driver.find_elements(
                By.CSS_SELECTOR,
                ".invalid-feedback"
            )

            for error in field_errors:

                if error.is_displayed() and error.text.strip():

                    logger.info(
                        f"Field validation error: {error.text}"
                    )

                    return error.text.strip()

        except Exception:

            logger.warning(
                "No field validation errors found"
            )

        # Generic error fallback
        try:

            error = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        "//*[contains(@class,'invalid-feedback') or "
                        "contains(@class,'alert') or "
                        "contains(@class,'error')]"
                    )
                )
            )

            if error.text.strip():

                logger.info(
                    f"Generic error found: {error.text}"
                )

                return error.text.strip()

        except Exception:

            logger.error(
                "No error message found on the page"
            )

            raise Exception(
                "No error message found on the page"
            )