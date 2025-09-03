import pytest

from pages.documents_template import Document_template


@pytest.mark.usefixtures("driver", "login")
class TestDocumentTemplatePage:

    def test_navigating_to_document_template(self, driver):
        document_template_page = Document_template(driver)
        document_template_page.navigating_to_template()

        # ✅ Verify we reached the correct URL
        current_url = document_template_page.get_current_url()
        print(f"Current URL after navigation: {current_url}")
        assert "official_documents" in current_url.lower() or "document" in current_url.lower()

        document_template_page.implementing_create_document()

        document_template_page.implementing_edit_flow()
        document_template_page.implementing_view()
        document_template_page.implementing_delete()
        document_template_page.implmenting_force_delete()




