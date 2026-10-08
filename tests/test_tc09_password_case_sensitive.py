import pytest


@pytest.mark.negative
def test_tc09_password_case_sensitive(account, login_page):
    login_page.fill(account.email, account.password.swapcase()).submit()
    assert login_page.error_message() == 'Your email or password is incorrect!'
    assert login_page.is_displayed()
    assert not login_page.has_authenticated_user()
