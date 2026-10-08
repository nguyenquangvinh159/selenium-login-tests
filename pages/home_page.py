from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    _ACCOUNT_NAME = (By.XPATH, '//a[contains(., "Logged in as")]/b')
    _LOGOUT = (By.CSS_SELECTOR, 'a[href="/logout"]')
    _LOGIN_LINK = (By.CSS_SELECTOR, 'a[href="/login"]')

    def wait_logged_in(self):
        self._visible(self._ACCOUNT_NAME)
        self._visible(self._LOGOUT)
        return self

    def logged_in_name(self):
        return self._visible(self._ACCOUNT_NAME).text

    def logout_is_visible(self):
        return self._visible(self._LOGOUT).is_displayed()

    def has_authenticated_user(self):
        return any(e.is_displayed() for locator in (self._ACCOUNT_NAME, self._LOGOUT)
                   for e in self.driver.find_elements(*locator))

    def login_link_is_visible(self):
        return self._visible(self._LOGIN_LINK).is_displayed()

    def logout(self):
        from pages.login_page import LoginPage
        self._click(self._LOGOUT)
        self.wait.until(lambda _: self.path == '/login')
        login = LoginPage(self.driver, self.base_url, self.timeout)
        login.is_displayed()
        return login

    def refresh(self):
        self.driver.refresh()
        return self.wait_logged_in()
