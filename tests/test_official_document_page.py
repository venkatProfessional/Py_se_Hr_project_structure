import pytest
from pages.Official_document_page import officialDocument


@pytest.mark.usefixtures("driver", "login")
class TestOfficialDocumentPage:

    def test_navigate_to_official_document(self, driver):
        """
        Navigate to the Official Document page and validate the navigation.

        Args:
            driver: The Selenium WebDriver instance.

        Returns:
            None
        """
        official_document_page = officialDocument(driver)
        official_document_page.navigate_official_document_page()
        official_document_page.Implement_offer_letter()
        official_document_page.Implement_Relieving_letter()
        official_document_page.Implement_termination_letter()
        official_document_page.implement_salary_revision_letter()
