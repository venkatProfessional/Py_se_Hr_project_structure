# test_employee_creation.py
import pytest

from pages.CMS_page import CMS_page



@pytest.mark.usefixtures("driver", "login")
class TestEmployeeCreation:

    def test_CMS_page(self, driver):
        page = CMS_page(driver)
        # Just call it without passing self or driver again
        page.navigate_to_cms_page()
        page.implementing_cms_create()

