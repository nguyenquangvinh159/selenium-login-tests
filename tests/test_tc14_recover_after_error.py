import pytest


@pytest.mark.positive
def test_tc14_recover_after_error(account, login_page):
    login_page.fill(account.email, account.password + '_wrong').submit()
    assert login_page.error_message() == 'Your email or password is incorrect!'
    assert not login_page.has_authenticated_user()
    home = login_page.login_as(account.email, account.password)
    assert home.logged_in_name() == account.name
    assert home.logout_is_visible()
