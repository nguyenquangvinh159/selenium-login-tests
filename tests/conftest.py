import os
import re
import warnings
from pathlib import Path

import pytest
import pytest_html
from selenium import webdriver

from pages.login_page import LoginPage
from support.accounts import AccountFactory

ROOT = Path(__file__).resolve().parents[1]


def pytest_addoption(parser):
    parser.addoption('--headed', action='store_true', help='Show Chrome (default: headless).')
    parser.addoption('--base-url', default=os.getenv('BASE_URL', 'https://automationexercise.com'))
    parser.addoption('--wait-timeout', type=float, default=20, help='Explicit wait timeout in seconds.')


@pytest.fixture
def base_url(request):
    return request.config.getoption('--base-url').rstrip('/')


@pytest.fixture
def browser_factory(request):
    browsers = []
    os.environ.setdefault('SE_CACHE_PATH', str(ROOT / '.selenium-cache'))
    os.environ.setdefault('SE_AVOID_STATS', 'true')

    def create():
        options = webdriver.ChromeOptions()
        if not request.config.getoption('--headed'):
            options.add_argument('--headless=new')
        options.add_argument('--window-size=1440,1000')
        options.page_load_strategy = 'eager'
        driver = webdriver.Chrome(options=options)
        browsers.append(driver)
        driver.implicitly_wait(0)
        driver.set_page_load_timeout(60)
        return driver

    yield create
    # Quit every browser, including a second isolated session opened by a test.
    errors = []
    for browser in reversed(browsers):
        try:
            browser.quit()
        except Exception as exc:
            errors.append(str(exc))
    if errors:
        raise RuntimeError('Browser teardown failed: ' + '; '.join(errors))


@pytest.fixture
def driver(browser_factory):
    return browser_factory()


@pytest.fixture
def login_page(driver, base_url, request):
    return LoginPage(driver, base_url, request.config.getoption('--wait-timeout')).open()


@pytest.fixture
def account(base_url):
    factory = AccountFactory(base_url)
    try:
        yield factory.create()
    finally:
        factory.cleanup()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.failed and report.when in ('setup', 'call'):
        driver = item.funcargs.get('driver')
        if driver:
            try:
                directory = ROOT / 'reports' / 'screenshots'
                directory.mkdir(parents=True, exist_ok=True)
                name = re.sub(r'[^a-zA-Z0-9_-]', '_', item.nodeid)
                picture = driver.get_screenshot_as_base64()
                driver.save_screenshot(str(directory / (name + '.png')))
                report.extras = getattr(report, 'extras', []) + [
                    pytest_html.extras.png(picture, name='Failure screenshot')
                ]
                report.sections.append(('Browser', 'URL: ' + driver.current_url))
            except Exception as exc:
                warnings.warn(f'Could not capture failure screenshot: {exc}', stacklevel=1)


def pytest_html_report_title(report):
    report.title = 'Selenium Python - Login test results'
