"""Shared explicit waits. Business assertions belong in test functions."""
from urllib.parse import urlparse

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver, base_url, timeout=20):
        self.driver = driver
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.wait = WebDriverWait(
            driver, timeout, ignored_exceptions=(StaleElementReferenceException,)
        )

    @property
    def path(self):
        return urlparse(self.driver.current_url).path

    def _visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def _click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def _type(self, locator, value):
        element = self._visible(locator)
        element.clear()
        element.send_keys(value)
