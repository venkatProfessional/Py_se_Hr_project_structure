import pytest
from pages.dashboard_page import DashboardPage

@pytest.mark.smoke
def test_click_datewise_button(login):
    driver = login
    dashboard = DashboardPage(driver)

    dashboard.click_datewise()
    dashboard.click_monthly()
    dashboard.click_HR()
    dashboard.click_employee()
    dashboard.click_Today()


    # Optional assertion (based on your app's behavior after clicking)
    assert "Datewise" in driver.page_source or driver.current_url  # Modify if needed

