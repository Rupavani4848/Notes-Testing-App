from selenium.common.exceptions import NoSuchElementException

from utils.logger import logger


class SelfHealingDriver:

    @staticmethod
    def find_element(driver, locators):

        for locator in locators:

            try:

                element = driver.find_element(*locator)

                logger.info(
                    f"Locator success: {locator}"
                )

                return element

            except NoSuchElementException:

                logger.warning(
                    f"Locator failed: {locator}"
                )

        logger.error(
            "All locators failed"
        )

        raise Exception(
            "Element not found using any locator"
        )