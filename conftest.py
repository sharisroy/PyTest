import os
from datetime import datetime

import pytest

# Hook to configure pytest and add a custom marker
def pytest_configure(config):
    # Add a custom marker that can be used across tests
    config.addinivalue_line(
        "markers", "smoke: mark test as part of the smoke test suite"
    )
    # time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    # report_dir = "reports"
    # report_file = f"My_Report_{time}.html"
    # if not os.path.exists(report_dir):
    #     os.makedirs(report_dir)
    # if not config.option.htmlpath:
    #     config.option.htmlpath = os.path.join(report_dir, report_file)

    if not config.option.htmlpath:
        config.option.htmlpath = "report/test_report.html"

# Hook to add custom metadata to the HTML report
@pytest.hookimpl(tryfirst=True)
def pytest_metadata(metadata):
    # Add custom metadata to the report
    metadata['Project Name'] = 'My Test Project'
    metadata['Module Name'] = 'API Tests'
    metadata['Tester'] = 'Haris'

# Hook to modify the title of the HTML report
def pytest_html_report_title(report):
    report.title = "My Project Test Report"

# Hook to modify the environment information in the HTML report
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([f"Project: My Test Project", "API Test Results"])
    postfix.extend(["Tester: Haris"])

# Session-scoped fixture to set up a test environment
@pytest.fixture(scope="session")
def setup_environment():
    print("\nSetting up the environment for all tests")
    yield
    print("\nTearing down the environment after all tests")

# Function-scoped fixture to provide mock data
@pytest.fixture(scope="function")
def mock_data():
    print("\nSetting up mock data for the test")
    data = {"key": "value", "number": 123}
    yield data
    print("\nTearing down mock data after the test")

# Hook to add test results to the HTML report
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # This hook is responsible for adding extra info to the HTML report
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' and report.failed:
        report.extra = getattr(report, 'extra', [])
        # Example: Add a screenshot or other extra information (commented out for now)
        # report.extra.append(pytest_html.extras.image('screenshot.png'))

# Hook to generate the HTML report
def pytest_sessionfinish(session, exitstatus):
    # You can add any final cleanup or reporting tasks here
    print(f"Tests finished with exit status: {exitstatus}")
