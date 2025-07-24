import pytest


@pytest.mark.suite("test Login Module")
def test_dashboard_title(login):
    driver = login
    assert "Dashboard" in driver.title or "Welcome" in driver.page_source
    print("Dashboard title",driver.title+"is displayed we entered into the dashboard page")
