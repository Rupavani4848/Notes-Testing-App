from pages.login_page import LoginPage

def test_login(driver, config):
    login = LoginPage(driver)
    login.login(config["user"]["email"], config["user"]["password"])

    assert "notes" in driver.current_url.lower()