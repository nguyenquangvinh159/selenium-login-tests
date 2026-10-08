import pytest


@pytest.mark.session
def test_tc20_isolated_browser_session(account, login_page, browser_factory, base_url):
    from pages.home_page import HomePage
    home = login_page.login_as(account.email, account.password)
    assert home.logged_in_name() == account.name
    other = HomePage(browser_factory(), base_url).open_anonymous()
    assert other.login_link_is_visible()
    assert not other.has_authenticated_user()
    assert home.logged_in_name() == account.name
    assert home.logout_is_visible()
