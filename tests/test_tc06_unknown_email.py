import pytest


@pytest.mark.negative
def test_tc06_unknown_email(login_page):
    from uuid import uuid4
    email = 'unregistered_' + uuid4().hex + '@example.com'
    login_page.fill(email, 'DummyPass9!').submit()
    assert login_page.error_message() == 'Your email or password is incorrect!'
    assert login_page.is_displayed()
    assert not login_page.has_authenticated_user()
