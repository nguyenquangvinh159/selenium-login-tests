import pytest


@pytest.mark.positive
def test_tc01_valid_login(account, login_page):
    """TC01: Correct credentials show the account name and Logout link."""
    home = login_page.login_as(account.email, account.password)

    assert home.logged_in_name() == account.name
    assert home.logout_is_visible()
    assert home.path == '/'
