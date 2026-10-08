import pytest


@pytest.mark.session
def test_tc16_session_after_refresh(account, login_page):
    home = login_page.login_as(account.email, account.password)
    assert home.logged_in_name() == account.name
    home.refresh()
    assert home.logged_in_name() == account.name
    assert home.logout_is_visible()
