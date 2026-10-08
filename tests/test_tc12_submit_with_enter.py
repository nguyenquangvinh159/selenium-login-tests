import pytest


@pytest.mark.positive
def test_tc12_submit_with_enter(account, login_page):
    login_page.fill(account.email, account.password)
    home = login_page.submit_with_enter()
    assert home.logged_in_name() == account.name
    assert home.logout_is_visible()
