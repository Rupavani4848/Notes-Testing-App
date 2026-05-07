import pytest
from pages.login_page import LoginPage


@pytest.mark.parametrize(
    "email,password,error_message",
    [
        ("wrongemail@gmail.com", "wrongpassword", "Incorrect email address or password"),
        ("", "", "Email address is required"),
        ("rupa0103@gmail.com", "", "Password is required"),

        ("invalidemail", "password123", "Email address is invalid"),
        ("", "password123", "Email address is required"),
        ("test@", "password123", "Email address is invalid"),

        ("' OR '1'='1", "' OR '1'='1", "Email address is invalid")
    ]
)
def test_invalid_login(driver, email, password, error_message):

    login = LoginPage(driver)

    login.open("https://practice.expandtesting.com/notes/app")

    login.login(email, password)

    error = login.get_error_message()

    assert error_message in error