import pytest


@pytest.mark.ui
def test_tc13_keyboard_navigation(account, login_page):
    login_page.focus_email()
    assert login_page.focused_field() == 'login-email'
    login_page.type_focused(account.email)
    login_page.press_tab()
    assert login_page.focused_field() == 'login-password'
    login_page.type_focused(account.password)
    login_page.press_tab()
    assert login_page.focused_field() == 'login-button'
    home = login_page.activate_focused_submit()
    assert home.logged_in_name() == account.name
    assert home.logout_is_visible()
