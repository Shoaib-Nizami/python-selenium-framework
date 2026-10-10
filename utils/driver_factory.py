"""
Driver Factory for creating WebDriver instances.
Supports Chrome and Firefox with configurable options.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from config.config import Config
from utils.logger import get_logger

logger = get_logger(__name__)


class DriverFactory:
    """Factory class to create WebDriver instances."""

    @staticmethod
    def get_driver(browser: str = Config.BROWSER, headless: bool = Config.HEADLESS):
        """
        Create and return a WebDriver instance.

        Args:
            browser: Browser name ('chrome' or 'firefox')
            headless: Run in headless mode if True

        Returns:
            WebDriver instance
        """
        browser = browser.lower()
        logger.info(f"Creating driver: browser={browser}, headless={headless}")

        if browser == "chrome":
            return DriverFactory._create_chrome_driver(headless)
        elif browser == "firefox":
            return DriverFactory._create_firefox_driver(headless)
        else:
            raise ValueError(f"Unsupported browser: {browser}. Use 'chrome' or 'firefox'.")

    @staticmethod
    def _create_chrome_driver(headless: bool):
        """Create a Chrome WebDriver instance."""
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-extensions")

        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )
        driver.implicitly_wait(Config.IMPLICIT_WAIT)
        logger.info("Chrome driver created successfully")
        return driver

    @staticmethod
    def _create_firefox_driver(headless: bool):
        """Create a Firefox WebDriver instance."""
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")

        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )
        driver.implicitly_wait(Config.IMPLICIT_WAIT)
        logger.info("Firefox driver created successfully")
        return driver
