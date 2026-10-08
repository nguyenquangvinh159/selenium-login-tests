import pytest


@pytest.mark.ui
def test_tc11_password_masked(login_page):
    login_page.fill('validation@example.com', 'MaskMe9!')
    assert login_page.password_input_type() == 'password'
    assert login_page.password_value() == 'MaskMe9!'
