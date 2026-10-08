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

    _PRODUCTS = (By.CSS_SELECTOR, 'a[href="/products"]')
    _HOME = (By.XPATH, '//header//a[contains(., "Home")]')

    def go_to_products(self):
        self._click(self._PRODUCTS)
        self.wait.until(lambda _: self.path == '/products')
        return self.wait_logged_in()

    def go_home(self):
        self._click(self._HOME)
        self.wait.until(lambda _: self.path == '/')
        return self.wait_logged_in()

    def current_tab(self):
        return self.driver.current_window_handle

    def tab_count(self):
        return len(self.driver.window_handles)

    def open_new_tab(self):
        self.driver.switch_to.new_window('tab')
        self.driver.get(self.base_url + '/')
        return self.wait_logged_in()

    def close_tab_and_return(self, original_tab):
        self.driver.close()
        self.driver.switch_to.window(original_tab)
        return self.wait_logged_in()

    def back_and_refresh(self):
        self.driver.back()
        self.driver.refresh()
        self._visible(self._LOGIN_LINK)
        return self

    def open_anonymous(self):
        self.driver.get(self.base_url + '/')
        self._visible(self._LOGIN_LINK)
        return self
