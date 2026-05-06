from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        element = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        try:
            element.click()
        except Exception as e:
            if "intercepted" in str(e).lower():
                self.driver.execute_script("arguments[0].click();", element)
            else:
                raise e

    def send_keys(self, locator, text):
        element = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def open(self, url):
        self.driver.get(url)