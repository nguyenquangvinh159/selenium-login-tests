import pytest


@pytest.mark.session
def test_tc17_session_navigation(account, login_page):
    home = login_page.login_as(account.email, account.password)
    home.go_to_products()
    assert home.path == '/products'
    assert home.logged_in_name() == account.name
    home.go_home()
    assert home.path == '/'
    assert home.logged_in_name() == account.name
    assert home.logout_is_visible()
