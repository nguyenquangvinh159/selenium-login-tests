import pytest


@pytest.mark.validation
def test_tc02_missing_password(login_page):
    """TC02: Native validation blocks submission with an empty password."""
    login_page.fill('validation@example.com', '').submit()

    validity = login_page.field_validity('password')
    assert validity['valueMissing'] and not validity['valid']
    assert validity['message']
    assert login_page.focused_field() == 'login-password'
    assert login_page.is_displayed()
