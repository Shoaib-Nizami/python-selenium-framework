"""
Pytest configuration and shared fixtures for the test suite.
"""

import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from config.config import Config
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.logger import get_logger

logger = get_logger(__name__)


def pytest_addoption(parser):
    """Add custom CLI options for browser, headless mode, and base URL."""
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests: chrome or firefox",
        choices=("chrome", "firefox")
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browser in headless mode"
    )
    parser.addoption(
        "--base-url",
        action="store",
        default=Config.BASE_URL,
        help="Base URL of the application under test"
    )


@pytest.fixture(scope="session")
def browser(request):
    """Get browser name from CLI option."""
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def headless(request):
    """Get headless flag from CLI option."""
    return request.config.getoption("--headless")


@pytest.fixture(scope="session")
def base_url(request):
    """Get base URL from CLI option."""
    return request.config.getoption("--base-url")


@pytest.fixture(scope="function")
def driver(browser, headless):
    """
    Create and yield a WebDriver instance per test function.
    Automatically quits the driver after each test.
    Supports Chrome and Firefox with headless mode.
    """
    logger.info(f"Starting {browser} browser | headless={headless}")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.implicitly_wait(Config.IMPLICIT_WAIT)
    driver.maximize_window()

    yield driver

    # Cleanup after each test
    logger.info("Quitting browser driver")
    driver.quit()


@pytest.fixture(scope="function")
def login_page(driver, base_url):
    """Navigate to base URL and return LoginPage instance."""
    driver.get(base_url)
    return LoginPage(driver)


@pytest.fixture(scope="function")
def inventory_page(driver):
    """Return InventoryPage instance."""
    return InventoryPage(driver)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Capture screenshot on test failure.
    Attaches screenshot path to the test report.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshot_dir = "reports/screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(
                screenshot_dir, f"{item.name}.png"
            )
            driver.save_screenshot(screenshot_path)
            logger.error(f"Screenshot saved: {screenshot_path}")
            report.extra = getattr(report, "extra", [])
