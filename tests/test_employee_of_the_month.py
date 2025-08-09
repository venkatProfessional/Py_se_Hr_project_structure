import time

import pytest
from pages.Employee_of_the_month import Employee_of_the_month


@pytest.mark.usefixtures("driver", "login")
class TestEmployeeOfTheMonth:

    def test_navigate_to_employee_of_month(self, driver):
        """
        ✅ Verify navigation to the 'Employee Of Month' section
        """
        page = Employee_of_the_month(driver)

        print("🔄 Navigating to 'Employee Of Month' section...")
        page.navigate_to_employee_of_month()

        # Add a short pause if required by UI transitions
        page.pause(1)

        # ✅ Validation - either by URL pattern or page content
        assert "employee-of-month" in driver.current_url.lower() or \
               "Employee Of Month" in driver.page_source, \
            "❌ Failed to navigate to Employee Of Month page"
        print("✅ Navigation successful.")
#         further steps

        page.test_employee_of_the_month()
        time.sleep(2)
        page.test_edit_employee_of_the_month()





