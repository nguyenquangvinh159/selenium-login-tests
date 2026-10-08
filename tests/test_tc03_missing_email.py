import pytest


@pytest.mark.validation
def test_tc03_missing_email(login_page):
    login_page.fill('', 'DummyPass9!').submit()
    validity = login_page.field_validity('email')
    assert validity['valueMissing'] and not validity['valid']
    assert validity['message']
    assert login_page.focused_field() == 'login-email'
    assert login_page.is_displayed()
