# Python Selenium Framework

> A production-grade test automation framework built with **Python 3.12**, **Selenium WebDriver**, and **Pytest**, following the **Page Object Model (POM)** design pattern.

[![Selenium Tests](https://github.com/Shoaib-Nizami/python-selenium-framework/actions/workflows/tests.yml/badge.svg)](https://github.com/Shoaib-Nizami/python-selenium-framework/actions/workflows/tests.yml)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.51-green)
![Pytest](https://img.shields.io/badge/Pytest-9.1-orange)
![Tests](https://img.shields.io/badge/tests-14%20passed-brightgreen)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| **Page Object Model (POM)** | Clean separation of page logic from test logic |
| **Pytest + Fixtures** | Powerful test setup, teardown, and dependency injection |
| **Multi-Browser Support** | Chrome and Firefox (headless & headed modes) |
| **Headless by Default** | Optimized for CI/CD and WSL/SSH environments |
| **Explicit Waits** | Smart, reliable element synchronization |
| **HTML Reports** | Self-contained pytest-html execution reports |
| **Screenshot on Failure** | Automatic screenshot capture for debugging |
| **GitHub Actions CI** | Automated test execution on every push and PR |
| **Structured Logging** | Console + file logging for traceability |
| **Environment-Based Config** | Override via env variables or `config.py` |
| **Parallel Execution** | Run tests across multiple workers with `pytest-xdist` |

---

## 📊 Test Results

**14 tests — All Passing** ✅

| Suite | Tests | Coverage |
|-------|-------|----------|
| `test_login.py` | 8 | Valid login, invalid credentials, locked user, empty fields |
| `test_inventory.py` | 6 | Page load, products display, cart, sorting, logout |
| **Total** | **14** | **✅ 100% Pass** |

**Demo site:** [saucedemo.com](https://www.saucedemo.com) — public Sauce Labs test site

---

## 📁 Project Structure

```
python-selenium-framework/
├── README.md
├── LICENSE
├── requirements.txt
├── pytest.ini
├── conftest.py                    # Pytest fixtures & CLI options
├── config/
│   └── config.py                  # Environment-based configuration
├── pages/                         # Page Objects
│   ├── base_page.py               # Common actions
│   ├── login_page.py              # Login page
│   └── inventory_page.py          # Products page
├── tests/
│   ├── test_login.py              # 8 login tests
│   └── test_inventory.py          # 6 inventory tests
├── utils/
│   ├── driver_factory.py          # WebDriver factory
│   └── logger.py                  # Logging utility
├── reports/                       # HTML reports (gitignored)
├── screenshots/                   # Failure screenshots (gitignored)
└── .github/
    └── workflows/
        └── tests.yml              # GitHub Actions CI
```

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.12 |
| Automation | Selenium WebDriver 4.51 |
| Test Runner | Pytest 9.1 |
| Reporting | pytest-html 4.2 |
| Parallelism | pytest-xdist 3.8 |
| Driver Management | webdriver-manager 4.1 |
| CI/CD | GitHub Actions |
| OS Support | Linux (headless), Windows, macOS |

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/Shoaib-Nizami/python-selenium-framework.git
cd python-selenium-framework
```

### 2. Create virtual environment

```bash
python3.12 -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run tests

```bash
# Run all tests (headless by default)
pytest

# Verbose output
pytest -v

# Parallel execution (4 workers)
pytest -n 4

# Specific test file
pytest tests/test_login.py -v

# Specific test
pytest tests/test_login.py::TestLogin::test_valid_login -v
```

---

## ⚙️ Configuration

Framework is **environment-driven**. Override via CLI or environment variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `BASE_URL` | Application under test | `https://www.saucedemo.com` |
| `BROWSER` | Default browser (`chrome` / `firefox`) | `chrome` |
| `HEADLESS` | Run in headless mode | `true` |
| `IMPLICIT_WAIT` | Implicit wait (seconds) | `10` |
| `EXPLICIT_WAIT` | Explicit wait (seconds) | `15` |

**Examples:**

```bash
# Run on Firefox
BROWSER=firefox pytest

# Override base URL
BASE_URL=https://example.com pytest

# Run in headed mode (requires display)
pytest --no-headless
```

---

## 🧪 Page Object Model

Each page has its own class in `pages/`:

- **`base_page.py`** — Common actions (click, type, wait, screenshot)
- **`login_page.py`** — Login page elements & actions
- **`inventory_page.py`** — Products page elements & actions

**Sample:**

```python
# tests/test_login.py
class TestLogin:

    def test_valid_login(self, login_page, inventory_page):
        login_page.login("standard_user", "secret_sauce")
        assert inventory_page.is_loaded()

    def test_invalid_login(self, login_page):
        login_page.login("invalid_user", "wrong_password")
        assert login_page.is_error_visible()
```

---

## 🔄 CI/CD — GitHub Actions

Every push and pull request triggers the test suite automatically:

- **OS**: Ubuntu latest
- **Python**: 3.12
- **Browser**: Chrome (headless)
- **Artifacts**: HTML reports uploaded per run

View workflow: [`.github/workflows/tests.yml`](.github/workflows/tests.yml)

---

## 📈 Reporting

HTML reports are generated on every test run:

```bash
pytest --html=reports/report.html --self-contained-html
```

Reports include:
- ✅ Test status (pass / fail / skip)
- ⏱ Execution time per test
- 📸 Screenshots on failure
- 🖥 Environment details
- 📝 Captured log output

---

## 🐧 WSL / Headless Linux Support

This framework works out of the box in **WSL**, **Docker**, and **SSH sessions** with no display (`$DISPLAY` empty). Chrome runs in headless mode by default with DNS resolver flags pre-configured to avoid `ERR_NAME_NOT_RESOLVED` errors.

---

## 👤 Author

**Muhammad Shoaib**
Senior SQA / Python Engineer | SDET | AIOps / DevOps / SysOps
Karachi, Pakistan

- GitHub: [@Shoaib-Nizami](https://github.com/Shoaib-Nizami)
- LinkedIn: [muhammad-shoaib-b08b56291](https://www.linkedin.com/in/muhammad-shoaib-b08b56291/)

---

## 📄 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for details.