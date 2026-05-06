import os
import yaml
import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime

# Configure logging
log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "../reports/logs")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(log_dir, f'test_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log')),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def config():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    config_path = os.path.join(base_dir, "config", "config.yaml")

    with open(config_path, "r") as file:
        return yaml.safe_load(file)


@pytest.fixture
def driver(config):
    logger.info("Starting Chrome WebDriver")
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.get(config["base_url"])
    logger.info(f"Navigated to {config['base_url']}")

    yield driver
    logger.info("Closing Chrome WebDriver")
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture screenshots on test failure"""
    outcome = yield
    rep = outcome.get_result()

    if rep.failed and call.when == "call":
        # Get the driver from the test
        if "driver" in item.fixturenames:
            driver = item.funcargs.get("driver")
            if driver:
                screenshot_dir = os.path.join(
                    os.path.dirname(os.path.dirname(__file__)),
                    "../reports/screenshots"
                )
                os.makedirs(screenshot_dir, exist_ok=True)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
                screenshot_path = os.path.join(screenshot_dir, f"{item.name}_{timestamp}.png")
                driver.save_screenshot(screenshot_path)
                logger.error(f"Test failed. Screenshot saved: {screenshot_path}")
                print(f"\n Screenshot saved to: {screenshot_path}")
                
                # Attach to Allure report if available
                try:
                    import allure
                    allure.attach(
                        driver.get_screenshot_as_png(),
                        name=f"Screenshot_{item.name}",
                        attachment_type=allure.attachment_type.PNG
                    )
                except ImportError:
                    pass  # Allure not installed, skip attachment