import time

import pytest

from pages.ConfigurationSalaryPage import ConfigurationSalaryPage


@pytest.mark.usefixtures("driver", "login")
class TestConfigurationPage:

    def test_navigating_to_salary(self, driver):
        """
        Test navigating to the Salary tab via Configuration page.
        """
        config_page = ConfigurationSalaryPage(driver)

        # Perform navigation
        config_page.Navigating_to_salary()

        # ✅ Validation: check URL or element presence
        # Example: ensure Salary page/tab is visible
        assert config_page.is_element_visible(config_page.salary_tab), "❌ Salary tab not visible!"

        print("✅ Successfully navigated to Salary tab.")

        time.sleep(4)

        config_page.update_salary_status()

        




