import pytest
from pages.EmailTemplatePage import EmailTemplatePage


@pytest.mark.usefixtures("driver", "login")
class TestEmailTemplatePage:

    def test_navigating_to_email_templates(self, driver):
        email_template_page = EmailTemplatePage(driver)
        email_template_page.navigating_to_email_templates()
