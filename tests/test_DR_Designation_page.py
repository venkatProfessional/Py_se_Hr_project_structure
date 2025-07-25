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

        with allure.step("🗑️ Handling Designation Delete and Restore Flow"):
            try:
                page.handledelete()
            except Exception as e:
                allure.attach(str(e), name="Handle Delete Error", attachment_type=allure.attachment_type.TEXT)
                screenshot = page.driver.get_screenshot_as_png()
                allure.attach(screenshot, name="Error Screenshot", attachment_type=allure.attachment_type.PNG)
                print(f"⚠️ Caught exception during delete handling: {e}")

    # @allure.title("🧪 Test: Delete and Restore Designation Flow")
    # @allure.severity(allure.severity_level.CRITICAL)
    # def test_delete_and_restore_designation(self,driver):
    #     """
    #     Test case to delete a designation, handle alert, restore it, and return to designation list.
    #     """
    #     page = DesignationPage(driver)
    #     with allure.step("🗑️ Handling Designation Delete and Restore Flow"):
    #         try:
    #             page.handle_designation_page()  # Navigate or setup if required
    #             page.handledelete()  # Perform delete + restore + back navigation
    #         except Exception as e:
    #             # Attach error message
    #             allure.attach(str(e), name="Handle Delete Error", attachment_type=allure.attachment_type.TEXT)
    #
    #             # Optional: Attach screenshot for debugging
    #             try:
    #                 screenshot = page.driver.get_screenshot_as_png()
    #                 allure.attach(screenshot, name="Error Screenshot", attachment_type=allure.attachment_type.PNG)
    #             except:
    #                 pass  # Skip screenshot if driver not available
    #
    #             print(f"⚠️ Caught exception during delete handling: {e}")
    #             # Optional: raise e if you want test to fail
