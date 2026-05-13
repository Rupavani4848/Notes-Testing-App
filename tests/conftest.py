import os
import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def config():
    with open("config/config.yaml") as file:
        return yaml.safe_load(file)

@pytest.fixture
def driver(config):

    options = Options()
    options.add_argument("--start-maximized")

    execution = os.getenv("EXECUTION", "local")

    print(f"\nRunning in: {execution}")

    if execution == "remote":

        driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            options=options
        )

    else:

        driver = webdriver.Chrome(options=options)

    driver.get(config["base_url"])

    yield driver

    driver.quit()