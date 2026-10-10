"""
Configuration settings for the test automation framework.
Environment-specific values can be overridden via CLI options or environment variables.
"""

import os


class Config:
    """Framework configuration constants."""

    # Application
    BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com")

    # Browser settings
    BROWSER = os.getenv("BROWSER", "chrome")
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"

    # Timeouts
    IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "10"))
    EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "15"))

    # Credentials (for demo purposes only - use secrets in production)
    VALID_USERNAME = os.getenv("VALID_USERNAME", "standard_user")
    VALID_PASSWORD = os.getenv("VALID_PASSWORD", "secret_sauce")
    LOCKED_USERNAME = os.getenv("LOCKED_USERNAME", "locked_out_user")
