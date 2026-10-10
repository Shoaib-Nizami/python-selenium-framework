"""
Test suite for Login functionality.
Covers valid login, invalid login, locked user, and empty credentials.
"""

import pytest
from config.config import Config


@pytest.mark.login
@pytest.mark.smoke
class TestLogin:
    """Test cases for the login page."""

    def test_valid_login(self, login_page, inventory_page):
        """Test successful login with valid credentials."""
        login_page.login(Config.VALID_USERNAME, Config.VALID_PASSWORD)
        assert inventory_page.is_on_inventory_page(),             "User should be redirected to inventory page after valid login"

    def test_invalid_login(self, login_page):
        """Test login failure with invalid credentials."""
        login_page.login("invalid_user", "wrong_password")
        assert login_page.is_error_message_displayed(),             "Error message should be displayed for invalid credentials"
        assert "Username and password do not match" in login_page.get_error_message(),             "Error message should indicate username/password mismatch"

    def test_locked_out_user(self, login_page):
        """Test login failure for a locked-out user account."""
        login_page.login(Config.LOCKED_USERNAME, Config.VALID_PASSWORD)
        assert login_page.is_error_message_displayed(),             "Error message should be displayed for locked out user"
        assert "locked out" in login_page.get_error_message().lower(),             "Error message should indicate the user is locked out"

    @pytest.mark.parametrize("username,password,expected_error", [
        ("", Config.VALID_PASSWORD, "Username is required"),
        (Config.VALID_USERNAME, "", "Password is required"),
        ("", "", "Username is required"),
    ])
    def test_empty_credentials(self, login_page, username, password, expected_error):
        """Test login with empty username and/or password fields."""
        login_page.login(username, password)
        assert login_page.is_error_message_displayed(),             f"Error message should be displayed when {expected_error}"
        assert expected_error in login_page.get_error_message(),             f"Error message should contain: {expected_error}"

    def test_login_page_elements_visible(self, login_page):
        """Test that all login page elements are visible on load."""
        assert login_page.is_on_login_page(),             "Username, password fields and login button should be visible"
