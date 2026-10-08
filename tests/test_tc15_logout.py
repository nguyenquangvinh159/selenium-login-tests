import pytest


@pytest.mark.session
def test_tc15_logout(account, login_page):
    home = login_page.login_as(account.email, account.password)
    assert home.logged_in_name() == account.name
    login = home.logout()
    assert login.is_displayed()
    assert not login.has_authenticated_user()
    assert home.login_link_is_visible()
