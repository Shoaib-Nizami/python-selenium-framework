"""
Base Page class containing common web element interactions.
All page classes should inherit from this class.
"""

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from config.config import Config
from utils.logger import get_logger

logger = get_logger(__name__)


class BasePage:
    """Base class for all page objects."""

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)
        self.base_url = Config.BASE_URL

    def open(self, url: str = ""):
        """Open a URL in the browser."""
        full_url = f"{self.base_url}{url}"
        logger.info(f"Opening URL: {full_url}")
        self.driver.get(full_url)

    def find_element(self, locator: tuple) -> WebElement:
        """Find a single element with explicit wait (visibility)."""
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            logger.error(f"Element not found: {locator}")
            raise

    def find_elements(self, locator: tuple) -> list:
        """Find all elements matching the locator with explicit wait."""
        try:
            return self.wait.until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            logger.error(f"Elements not found: {locator}")
            raise

    def click(self, locator: tuple):
        """Click an element after waiting for it to be clickable."""
        logger.info(f"Clicking element: {locator}")
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def enter_text(self, locator: tuple, text: str):
        """Clear and type text into an input field."""
        logger.info(f"Entering text into {locator}: {text}")
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: tuple) -> str:
        """Get the visible text of an element."""
        return self.find_element(locator).text

    def is_element_visible(self, locator: tuple) -> bool:
        """Check if an element is visible on the page."""
        try:
            return self.find_element(locator).is_displayed()
        except (TimeoutException, NoSuchElementException):
            return False

    def is_element_present(self, locator: tuple) -> bool:
        """Check if an element is present in the DOM."""
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def get_page_title(self) -> str:
        """Return the current page title."""
        return self.driver.title

    def get_current_url(self) -> str:
        """Return the current browser URL."""
        return self.driver.current_url

    def wait_for_element_to_disappear(self, locator: tuple):
        """Wait until an element is no longer visible."""
        self.wait.until(EC.invisibility_of_element_located(locator))

    def take_screenshot(self, name: str):
        """Capture a screenshot and save it."""
        path = f"reports/screenshots/{name}.png"
        self.driver.save_screenshot(path)
        logger.info(f"Screenshot saved: {path}")
