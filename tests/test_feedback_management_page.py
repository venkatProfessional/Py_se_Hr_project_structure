import pytest

from pages.feedbackManagment_page import FeedbackManagmentPage


@pytest.mark.usefixtures("driver", "login")
class TestFeedbackManagementPage:

    def test_implementing_feedback_list(self, driver):
        page = FeedbackManagmentPage(driver)
        page.navigate_to_feedback_management()
        page.open_feedback_list()
        page.implement_create_feedback()
        page.implement_edit_feedback()
        page.delete_feedback()
        page.delete_feedback_permanently()
        page.Implementing_view_response()
        # Assertion: category tab should be visible
        # assert driver.find_element(*page.feedback_category).is_displayed()

    def test_implementing_feedback_category(self, driver):
        page = FeedbackManagmentPage(driver)
        page.navigate_to_feedback_management()
        page.open_feedback_category()
        page.implementing_categories_create()
        page.implementing_categories_edit()
        page.implementing_categories_delete()

        


