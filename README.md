# Nodus UI Automation Tests

UI automation project for Nodus Messenger built with **Python**, **Playwright**, and **Pytest** using the **Page Object Model (POM)** design pattern.

---

## Tech Stack
* **Language:** Python 3.12+
* **Framework:** Pytest
* **UI Driver:** Playwright
* **Pattern:** Page Object Model (POM)
* **CI/CD:** GitHub Actions
* **Reporting:** Allure Reports / JUnit XML

---

## Features
* **Multi-Language Testing:** Parametrized test execution using localized browser contexts (Russian / English).
* **Data-Driven Architecture:** Decoupled test logic and environments.
* **Secure Credentials Handling:** Complete isolation of sensitive data using environment variables.
* **CI/CD Integrated:** Automated test execution on repository events via GitHub Actions.
* **Parallel Execution:** Native support for distributed testing to reduce execution time.

---

## Project Structure
```text
NODUS-TESTS
├── .github/workflows/
│   └── playwright.yml       # CI/CD Pipeline
├── pages/                   # Page Object Layer
│   ├── login_page.py
│   ├── profile_page.py
│   └── registration_page.py
├── tests/                   # Test Suite Layer
│   ├── test_profile_settings.py
│   ├── test_sign_in.py
│   └── test_sign_up.py
├── .env.example             # Template for environment variables
├── .gitignore
├── conftest.py              # Global fixtures & localization hooks
├── pytest.ini               # Pytest configuration
├── README.md
└── requirements.txt

```

---

## Installation & Setup

1. **Clone the repository:**
```bash
git clone [https://github.com/your-username/nodus-tests.git](https://github.com/your-username/nodus-tests.git)
cd nodus-tests
```

2. **Create and activate a virtual environment:**
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
playwright install chromium --with-deps
```

4. **Configure Environment Variables:**
Create a `.env` file in the root directory (do not commit it to Git) and populate it with your test credentials:
```env
NODUS_LOGIN=your_test_username
NODUS_PASSWORD=your_test_password
```

---

## 🧪 Running Tests

**Run the complete test suite:**

```bash
pytest
```

**Run specific test modules:**
```bash
pytest tests/test_sign_up.py          # Registration only
pytest tests/test_sign_in.py          # Authentication only
pytest tests/test_profile_settings.py # Profile management
```

**Run tests in parallel with Allure report generation:**
```bash
pytest -n 2 --alluredir=allure-results
```

---

## Roadmap

* [x] Registration & Authentication E2E tests
* [x] Profile management and display name tests
* [x] Cross-language localization testing (RU/EN)
* [x] GitHub Actions CI Integration
* [x] Environment variable protection layer
* [ ] Session storage state sharing (API login bypass for performance optimization)

---

##  Author

**Artyom Berestov**

QA Automation Engineer | Python • Playwright • API Testing • CI/CD
