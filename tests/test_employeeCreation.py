# test_employee_creation.py
import pytest
from pages.EmployeeCreation_Page import EmployeeCreationPage

@pytest.mark.usefixtures("driver", "login")
class TestEmployeeCreation:

    def test_employee_creation(self, driver):
        page = EmployeeCreationPage(driver)
        # Just call it without passing self or driver again
        page.navigating_employee_list()
        # page.fill_basic_fields()
        # page.salary_info_field()

        page.fill_basic_details_from_json()
        # page.salary_info_field_excel()



    