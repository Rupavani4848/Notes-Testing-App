from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger


class SmartWaits:

    @staticmethod
    def wait_for_visibility(driver, locator, timeout=10):

        logger.info(f"Waiting for visibility: {locator}")

        return WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @staticmethod
    def wait_for_clickable(driver, locator, timeout=10):

        logger.info(f"Waiting for clickable: {locator}")

        return WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @staticmethod
    def wait_for_page_load(driver, timeout=20):

        WebDriverWait(driver, timeout).until(
            lambda d: d.execute_script(
                "return document.readyState"
            ) == "complete"
        )

        logger.info("Page loaded completely")