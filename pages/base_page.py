from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.logger import logger
from utils.retry_handler import retry
from utils.self_healing import SelfHealingDriver


class BasePage:

    def __init__(self, driver):

        self.driver = driver

    def find_element(self, locator, timeout=15):

        """
        Supports:
        1. Single locator tuple
        2. Multiple locators list (self-healing)
        """

        # Self-healing locators
        if isinstance(locator, list):

            logger.info("Trying self-healing locators")

            return SelfHealingDriver.find_element(
                self.driver,
                locator
            )

        # Normal locator
        logger.info(f"Finding element: {locator}")

        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @retry(max_attempts=3, delay=2)
    def click(self, locator):

        element = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(
                locator[0] if isinstance(locator, list) else locator
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            element
        )

        logger.info(f"Clicking element: {locator}")

        try:

            element.click()

        except Exception as e:

            if "intercepted" in str(e).lower():

                logger.warning(
                    "Click intercepted. Using JavaScript click."
                )

                self.driver.execute_script(
                    "arguments[0].click();",
                    element
                )

            else:
                raise e

    @retry(max_attempts=3, delay=2)
    def send_keys(self, locator, text):

        element = self.find_element(locator)

        logger.info(f"Entering text into: {locator}")

        element.clear()
        element.send_keys(text)

    def open(self, url):

        logger.info(f"Opening URL: {url}")

        self.driver.get(url)