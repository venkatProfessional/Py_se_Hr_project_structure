import allure
import pytest
from pages.Employee_type_History import  EmployeeTypeHistory


@pytest.mark.usefixtures("driver", "login")
class TestEmployeeTypeHistory:

    @allure.title("implementing employee type history")
    def test_implementing_employee_type_history(self, driver):
        page = EmployeeTypeHistory(driver)
        page.navigating_to_employee_type_history()
        page.validating_search_bar()
        page.Validating_view_button()
        page.navigatingtosalaryrevision()
        page.check_history_and_download()
        page.navigating_Employee_Assets()

