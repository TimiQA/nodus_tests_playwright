# Nodus UI Automation Tests

UI automation project for **Nodus Messenger** built with **Python**, **Playwright**, and **Pytest** using the **Page Object Model (POM)** design pattern.

## Tech Stack

- Python
- Playwright
- Pytest
- Page Object Model (POM)
- Git

## Features

- UI end-to-end testing
- Page Object Model architecture
- Localization testing (Russian / English)
- Reusable Pytest fixtures
- Scalable project structure

## Project Structure

```text
.
├── .github/
│   └── workflows/
│       └── playwright.yml
├── pages/
│   ├── login_page.py
│   ├── profile_page.py
│   └── registration_page.py
├── test_profile_settings.py
├── test_sign_in.py
├── test_sign_up.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Installation

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

**Linux / macOS**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

Install project dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

## Running Tests

Run all tests:

```bash
pytest
```

Run registration tests only:

```bash
pytest test_sign_up.py
```

Run login tests only:

```bash
pytest test_sign_in.py
```
Run tests in parallel (2 workers) and generate Allure results
```bash
pytest -n 2 --alluredir=allure-results
```

## Roadmap

- [x] Registration tests
- [x] Login tests
- [x] Profile settings tests
- [x] GitHub Actions CI
- [x] Allure reports
- [x] Parallel test execution

## Author

**Artyom Berestov**

QA Engineer | Python • Playwright • API Testing • Test Automation