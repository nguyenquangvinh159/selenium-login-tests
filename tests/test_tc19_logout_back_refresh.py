import pytest


@pytest.mark.session
def test_tc19_logout_back_refresh(account, login_page):
    home = login_page.login_as(account.email, account.password)
    login = home.logout()
    assert login.is_displayed()
    home.back_and_refresh()
    assert home.login_link_is_visible()
    assert not home.has_authenticated_user()
