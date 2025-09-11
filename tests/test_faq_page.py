# test_employee_creation.py
import pytest
from pages.FAQ_page import FAQ_page


@pytest.mark.usefixtures("driver", "login")
class TestFAQCreation:

    def test_FAQ_page(self, driver):
        page =FAQ_page(driver)
        # Just call it without passing self or driver again
        page.navigate_to_FAQ_page()
        page.create_faqs()
        page.edit_faq()
        page.implementing_faq_delete_restore()
        page.implementing_faq_delete_permanently()




