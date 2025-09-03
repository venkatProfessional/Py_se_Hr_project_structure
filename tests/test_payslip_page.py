import pytest
from selenium.webdriver.common.by import By

import pages.pay_slip_page
from pages.pay_slip_page import PaySlipPage


@pytest.mark.usefixtures("driver", "login")  # Assuming you have a fixture for driver
class TestPaySlipPage:

    def test_navigating_to_payslip(self, driver):
        """
        Test case: Verify navigation to Payslip page.
        """
        page = PaySlipPage(driver)

        # Navigate to Payslip page
        page.navigatingtopayslip()

        # Add validation here (example: check if URL or element is correct)
        assert "payslip" in driver.current_url.lower() or \
               page.is_element_present(page.AdvanceTab), \
               "Failed to navigate to Payslip page"

        page.implementing_generate_payslip()

        # # Step 4: Assertions called directly from BasePage
        # page.assert_input_value(PaySlipPage.select_payslip_month, "July 2025")
        # page.assert_url_contains("payslip")
        # page.assert_element_visible(PaySlipPage.AdvanceTab)
