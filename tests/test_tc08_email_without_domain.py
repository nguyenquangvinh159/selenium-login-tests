import pytest


@pytest.mark.validation
def test_tc08_email_without_domain(login_page):
    login_page.fill('abc@', 'DummyPass9!').submit()
    validity = login_page.field_validity('email')
    assert validity['typeMismatch'] and not validity['valid']
    assert validity['message']
    assert login_page.focused_field() == 'login-email'
    assert login_page.is_displayed()
