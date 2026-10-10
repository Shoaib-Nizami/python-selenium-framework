"""
Login Page Object Model.
Contains locators and actions for the login page.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page object for the login page of SauceDemo."""

    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    BOTTLENECK_IMAGE = (By.CLASS_NAME, "bot_column")

    def enter_username(self, username: str):
        """Enter username in the username field."""
        self.enter_text(self.USERNAME_INPUT, username)

    def enter_password(self, password: str):
        """Enter password in the password field."""
        self.enter_text(self.PASSWORD_INPUT, password)

    def click_login_button(self):
        """Click the login button."""
        self.click(self.LOGIN_BUTTON)

    def login(self, username: str, password: str):
        """Complete login action with username and password."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def get_error_message(self) -> str:
        """Return the error message text if present."""
        return self.get_text(self.ERROR_MESSAGE)

    def is_error_message_displayed(self) -> bool:
        """Check if error message is displayed."""
        return self.is_element_visible(self.ERROR_MESSAGE)

    def is_on_login_page(self) -> bool:
        """Verify that the login page is loaded."""
        return (
            self.is_element_visible(self.USERNAME_INPUT) and
            self.is_element_visible(self.PASSWORD_INPUT) and
            self.is_element_visible(self.LOGIN_BUTTON)
        )

    def is_logged_in(self) -> bool:
        """Check if login was successful by verifying URL change."""
        return "inventory" in self.get_current_url()
