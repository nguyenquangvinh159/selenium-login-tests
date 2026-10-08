import pytest


@pytest.mark.session
def test_tc18_session_new_tab(account, login_page):
    home = login_page.login_as(account.email, account.password)
    original_tab = home.current_tab()
    home.open_new_tab()
    assert home.current_tab() != original_tab
    assert home.tab_count() == 2
    assert home.logged_in_name() == account.name
    home.close_tab_and_return(original_tab)
    assert home.tab_count() == 1
    assert home.logged_in_name() == account.name
