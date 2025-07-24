import allure
import pytest
import time
from pages.dashboard_page import DashboardPage
from pages.base_page import BasePage

@allure.feature("Dashboard Module")
@allure.story("HR user filters and views dashboard by Date, Month, HR, and Employee")
@allure.title("Smoke Test - Datewise Filter and Dashboard Card Navigation")
@allure.description("""
This test verifies that a user can apply various filters on the HR Dashboard 
(Datewise, Monthly, HR, Employee, Today) and that all dashboard cards navigate correctly.
""")
@pytest.mark.smoke
# @pytest.mark.skip(reason="Temporarily disabling this test")tes
def test_click_datewise_button(login):
    driver = login
    dashboard = DashboardPage(driver)

    dashboard.click_datewise()
    BasePage.wait()


    dashboard.click_monthly()
    BasePage.wait()

    dashboard.click_HR()
    BasePage.wait()

    dashboard.click_employee()
    BasePage.wait()

    dashboard.click_today()
    BasePage.wait()

    dashboard.check_navigation_for_all_dashboard_cards()
    # assert "User Management" in driver.page_source or driver.current_url  # Modify if needed
