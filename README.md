# Open Source Quality Intelligence - Pytest

A Selenium + Python + Pytest hybrid automation framework for the ExpandTesting Notes App, covering UI testing, API testing, end-to-end validation, parallel execution, reporting, and CI/CD-ready execution.

## Project Overview

This project is a capstone automation solution designed for the Notes application available at:

- UI: https://practice.expandtesting.com/notes/app
- API: https://practice.expandtesting.com/notes/api/api-docs

The framework supports:
- UI automation using Selenium WebDriver.
- API automation using Python Requests.
- Hybrid end-to-end validation between UI and API.
- Parallel execution using pytest-xdist.
- Reporting using Allure or HTML reports.
- Screenshot capture and logging.
- CI/CD integration with Jenkins.
- Advanced quality engineering concepts such as agentic workflows and intelligent locator handling.

## Objectives

- Validate login, note creation, deletion, and synchronization between UI and API.
- Build a scalable and maintainable automation framework using Page Object Model.
- Support reusable test utilities, fixtures, and centralized configuration.
- Enable advanced execution features such as parallel runs and reporting.
- Demonstrate manual test planning, scenarios, test cases, and requirement traceability.

## Features

- UI test automation with Selenium.
- API test automation with Requests.
- Hybrid UI + API end-to-end scenarios.
- Pytest framework with reusable fixtures.
- Page Object Model structure.
- Parallel test execution.
- Screenshot on failure.
- Structured logging.
- Allure/HTML reporting.
- CI/CD pipeline support.
- Performance checks for API response time.

## Functional Coverage

This project covers the following core requirements:

- UI login works successfully.
- User can create a note through the UI.
- Newly created note appears instantly in the UI list.
- GET notes API returns note data correctly.
- UI-created note is available in API response.
- Notes can be deleted through the API.
- Deleted notes disappear from the UI.
- Negative scenarios for invalid UI and API inputs.
- API response time validation.

## Suggested Project Structure

```bash
# Open Source Quality Intelligence - Notes Automation Framework

## Project Structure

```bash

├── api/
│   ├── __init__.py
│   ├── api_client.py
│   └── auth.py
├── config/
│   ├── __pycache__/
│   ├── config.yaml
│   ├── constants.py
│   └── environment.py
├── data/
├── fixtures/
│   ├── __init__.py
│   └── api_fixture.py
├── pages/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   └── notes_page.py
├── reports/
│   ├── allure-results/
│   ├── logs/
│   └── report.html
├── tests/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_api_to_ui.py
│   ├── test_create_note.py
│   ├── test_delete_note.py
│   ├── test_empty_note.py
│   ├── test_get_notes.py
│   ├── test_invalid_login.py
│   ├── test_login.py
│   ├── test_performance.py
│   └── test_ui_to_api.py
├── utils/
│   ├── __pycache__/
│   ├── __init__.py
│   └── api_client.py
├── venv/
├── .gitignore
├── pytest.ini
├── README.md
├── report.html
└── requirements.txt

```

## Prerequisites

- Python 3.10+
- pip
- Chrome browser
- ChromeDriver or WebDriver Manager
- Git

## Installation

Clone the repository:

```bash
git clone <your-repo-url>
cd <your-project-folder>
```

Create and activate a virtual environment:

### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Dependencies

Example `requirements.txt`:

```txt
pytest
selenium
requests
pytest-xdist
webdriver-manager
allure-pytest
python-dotenv
PyYAML
```

## Configuration

Create a `.env` or `config.yaml` file for environment settings such as:

```yaml
base_url: https://practice.expandtesting.com/notes/app
api_url: https://practice.expandtesting.com/notes/api
browser: chrome
headless: false
```

## Running Tests

Run all tests:

```bash
pytest
```

Run tests in parallel:

```bash
pytest -n auto
```

Run specific test file:

```bash
pytest tests/test_notes_ui.py
```

Generate Allure results:

```bash
pytest --alluredir=allure-results
```

Open Allure report:

```bash
allure serve allure-results
```

## Test Coverage

### UI Tests
- Login validation.
- Create note.
- Delete note.
- Verify note appears in UI list.

### API Tests
- GET notes.
- Create note.
- Delete note.
- Validate response status and payload.

### E2E Tests
- Create note in UI and verify in API.
- Delete note in API and verify removal from UI.

### Negative Tests
- Invalid login.
- Missing fields.
- Incorrect API requests.
- Validation of error messages and status codes.

## Reporting

The framework supports:
- Allure reports.
- HTML reports.
- Screenshots for failed UI tests.
- API response attachments.
- Logs for debugging and traceability.

## CI/CD Integration

Example Jenkins pipeline stages:
- Checkout code.
- Install dependencies.
- Run tests.
- Publish reports.
- Archive screenshots and logs.

## Traceability

The project includes:
- Requirement mapping.
- Test scenarios.
- Test cases.
- RTM to ensure full coverage of functional requirements.

## Deliverables

- Manual test plan.
- Test scenarios and test cases.
- Requirement Traceability Matrix.
- Selenium Python Pytest automation framework.
- UI + API hybrid test suite.
- Parallel execution support.
- Reporting and CI/CD setup.

