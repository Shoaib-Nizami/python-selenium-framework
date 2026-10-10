# Python Selenium Framework

> A robust and scalable test automation framework built with **Python**, **Selenium WebDriver**, and **Pytest** using the **Page Object Model (POM)** design pattern.

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.x-green)](https://www.selenium.dev/)
[![Pytest](https://img.shields.io/badge/Pytest-latest-orange)](https://docs.pytest.org/)
[![CI](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-brightgreen)](.github/workflows/tests.yml)

---

## Features

| Feature | Description |
|---------|-------------|
| **Page Object Model (POM)** | Clean separation of page logic from test logic |
| **Pytest + Fixtures** | Powerful test setup, teardown, and dependency injection |
| **Multi-Browser Support** | Chrome and Firefox (headless & headed modes) |
| **Explicit Waits** | Smart, reliable element synchronization |
| **Data-Driven Testing** | JSON and CSV-based test data support |
| **HTML Reports** | Beautiful pytest-html test execution reports |
| **Screenshot on Failure** | Automatic screenshot capture when a test fails |
| **GitHub Actions CI** | Automated test execution on every push and PR |
| **Logging** | Structured logging for debugging and traceability |
| **Configurable** | Environment-based configuration management |

---

## Project Structure

```
python-selenium-framework/
├── README.md
├── requirements.txt
├── pytest.ini
├── conftest.py
├── config/
│   └── config.py
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   └── inventory_page.py
├── tests/
│   ├── test_login.py
│   └── test_inventory.py
├── utils/
│   ├── driver_factory.py
│   └── logger.py
├── reports/
│   └── (generated HTML reports)
└── .github/
    └── workflows/
        └── tests.yml
```

---

## Tech Stack

- **Python 3.9+**
- **Selenium WebDriver 4.x**
- **Pytest** (test runner)
- **pytest-html** (HTML reporting)
- **pytest-xdist** (parallel test execution)
- **WebDriver Manager** (automatic driver management)
- **GitHub Actions** (CI/CD)

---

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/Shoaib-Nizami/python-selenium-framework
cd python-selenium-framework
```

### 2. Create a Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Tests

```bash
# Run all tests
pytest

# Run with HTML report
pytest --html=reports/report.html --self-contained-html

# Run in parallel (4 workers)
pytest -n 4

# Run specific test file
pytest tests/test_login.py -v

# Run in headless mode
pytest --headless

# Run on Firefox
pytest --browser=firefox
```

---

## Configuration

Edit `config/config.py` to customize:

| Variable | Description | Default |
|----------|-------------|---------|
| `BASE_URL` | Application under test | `https://www.saucedemo.com` |
| `BROWSER` | Default browser | `chrome` |
| `HEADLESS` | Run in headless mode | `False` |
| `IMPLICIT_WAIT` | Implicit wait timeout | `10` |
| `EXPLICIT_WAIT` | Explicit wait timeout | `15` |

You can also override via CLI:
```bash
pytest --browser=firefox --headless --base-url=https://example.com
```

---

## Page Object Model (POM)

Each page of the application has its own class in the `pages/` directory:

- **`base_page.py`** - Common actions (click, send_keys, wait, screenshots)
- **`login_page.py`** - Login page elements and actions
- **`inventory_page.py`** - Inventory/product page elements and actions

This pattern keeps tests clean, maintainable, and reusable.

---

## Sample Test

```python
# tests/test_login.py

class TestLogin:

    def test_valid_login(self, login_page, inventory_page):
        login_page.login("standard_user", "secret_sauce")
        assert inventory_page.is_on_inventory_page()

    def test_invalid_login(self, login_page):
        login_page.login("invalid_user", "wrong_password")
        assert login_page.get_error_message() ==                "Epic sadface: Username and password do not match"
```

---

## Data-Driven Testing

Tests can be driven by JSON or CSV files:

```python
# tests/test_login.py
import pytest
from utils.data_reader import read_json

@pytest.mark.parametrize("data", read_json("login_data.json"))
def test_login_with_json_data(self, login_page, data):
    login_page.login(data["username"], data["password"])
    assert login_page.is_logged_in() == data["expected"]
```

---

## CI/CD - GitHub Actions

Every push and pull request triggers the test suite automatically on:
- Ubuntu (latest)
- Python 3.9, 3.10, 3.11
- Chrome & Firefox (headless)

Test results and HTML reports are uploaded as artifacts.

See `.github/workflows/tests.yml` for the full pipeline configuration.

---

## Reporting

After test execution, an HTML report is generated in the `reports/` folder:

```bash
pytest --html=reports/report.html --self-contained-html
```

Reports include:
- Test status (pass/fail/skip)
- Execution time per test
- Screenshots on failure
- Environment details
- Log output

---

## Author

**Muhammad Shoaib**
- Senior SQA / Python Engineer | SDET
- AIOps / DevOps / SysOps
- Karachi, Pakistan

- [LinkedIn](https://pk.linkedin.com/in/muhammad-shoaib-b08b56291)

---

## License

This project is open-source and available under the [MIT License](LICENSE).
