import pytest
from selenium import webdriver

from pages.AdvancePage import AdvanceMaintanencePage


@pytest.mark.usefixtures("driver", "login") # Assumes a pytest fixture for driver setup
class TestAdvanceMaintanencePage:

    def test_navigate_to_advance(self, driver):
        page = AdvanceMaintanencePage(driver)
        page.navigatetoAdvance()

        expected_url_fragment = "https://smiligencehr.itsfortesza.com/advance"
        assert expected_url_fragment in driver.current_url, \
            f"Navigation to Advance tab failed. Current URL: {driver.current_url}"

        page.implementingCreateAdvanceAmount()

