import pytest
from selenium.webdriver.common.by import By
from pages.reminder_page import reminder_page

@pytest.mark.usefixtures("driver", "login")
class TestReminderPage:

    def test_navigating_to_reminder_page(self, driver):
        reminder_page_obj = reminder_page(driver)
        reminder_page_obj.navigating_to_reminder_page()

        # ✅ Verify we reached the correct URL
        current_url = reminder_page_obj.get_current_url()
        print(f"Current URL after navigation: {current_url}")
        assert "reminder" in current_url.lower()

        # create
        reminder_page_obj.implementing_create1()

        # ✅ Verify reminder creation
        # Option 1: Check for a success message (assuming the page shows a success message after submission)
        success_message_locator = (By.XPATH, "//div[@id='flashMessageMessage']")
        current_url = reminder_page_obj.get_current_url()
        print(f"Current URL after navigation: {current_url}")
        assert "https://smiligencehr.itsfortesza.com/reminder" in current_url.lower()
        assert reminder_page_obj.is_element_present(
            success_message_locator), "Success message not found after creating reminder"

        # Option 2: Verify the reminder appears in a list (assuming a table or list displays reminders)
        reminder_name_locator = (By.XPATH,
                                 "//td[contains(text(),'test 2')]")  # Adjust XPath based on actual page structure
        assert reminder_page_obj.is_element_present(
            reminder_name_locator), "Reminder with name 'test' not found in the list"

        # delete
        reminder_page_obj.implementing_delete()
        reminder_page_obj.implementing_edit()


        # assert reminder_page_obj.is_element_present(
        #     success_message_locator), "Success message not found after deleting reminder"










