import pytest


@pytest.mark.validation
def test_tc04_both_fields_empty(login_page):
    login_page.fill('', '').submit()
    assert login_page.field_validity('email')['valueMissing']
    assert login_page.field_validity('password')['valueMissing']
    assert login_page.focused_field() == 'login-email'
    assert login_page.is_displayed()
