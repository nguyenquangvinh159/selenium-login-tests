from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.home_page import HomePage


class LoginPage(BasePage):
    _EMAIL = (By.CSS_SELECTOR, '[data-qa="login-email"]')
    _PASSWORD = (By.CSS_SELECTOR, '[data-qa="login-password"]')
    _SUBMIT = (By.CSS_SELECTOR, '[data-qa="login-button"]')
    _ERROR = (By.CSS_SELECTOR, '.login-form p')

    def open(self):
        self.driver.get(self.base_url + '/login')
        self._visible(self._EMAIL)
        return self

    def fill(self, email, password):
        self._type(self._EMAIL, email)
        self._type(self._PASSWORD, password)
        return self

    def submit(self):
        self._click(self._SUBMIT)
        return self

    def login_as(self, email, password):
        self.fill(email, password).submit()
        return HomePage(self.driver, self.base_url, self.timeout).wait_logged_in()

    def error_message(self):
        return self._visible(self._ERROR).text

    def is_displayed(self):
        return self.path == '/login' and self._visible(self._EMAIL).is_displayed()
