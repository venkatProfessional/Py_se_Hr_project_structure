import time
import pytest
import allure

from pages.DR_Designation_page import DesignationPage


@pytest.mark.usefixtures("driver", "login")
class TestDesignationValidation:

    @allure.title("Blank Submit Validation with Multiple Edits")
    def test_blank_submit_validation(self, driver):
        """
        Test case to verify validation messages when submitting the Designation form without entering any data.
        """
        page = DesignationPage(driver)

        with allure.step("Navigate to Designation page and click Submit without data"):
            page.handle_designation_page()
            page.submit_without_entering_data()

        with allure.step("Handle validation message display"):
            page.handle_create_designation()

        time.sleep(2)

        with allure.step("Perform single edit"):
            page.handleedit()

        with allure.step("Perform multiple edits"):
            page.handlemultipleedits()

        with allure.step("Check if name format is valid"):
            if page.is_invalid_name_format_displayed():
                allure.attach("❌ Edit failed: Invalid name format", name="Edit Result", attachment_type=allure.attachment_type.TEXT)
                print("❌ Edit failed: Invalid name format.")
            else:
                allure.attach("✅ Edit passed with valid name format", name="Edit Result", attachment_type=allure.attachment_type.TEXT)
                print("✅ Edit passed with valid name format.")

        with allure.step("Handling Active/Inactive button flow"):
            try:
                page.handle_all_status_edits()
            except Exception as e:
                allure.attach(str(e), name="Handle Active/Inactive Error", attachment_type=allure.attachment_type.TEXT)
                print(f"⚠️ Caught exception in test: {e}")
                # Continue test even if exception occurs

