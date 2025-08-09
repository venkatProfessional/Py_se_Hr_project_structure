import pytest
from pages.task_maintanence_page import task_maintanence_page

@pytest.mark.usefixtures("driver", "login")
class TestTaskMaintenance:

    def test_navigate_to_task_maintenance_page(self, driver):
        print("🔍 Starting test: Navigate to Task Maintenance Page")
        page = task_maintanence_page(driver)
        page.navigate_to_task_maintanence_page()
        print("✅ Navigation successful")
        page.handle_load_test_data_from_json(
            "C:\\Users\\User\\PycharmProjects\\SmiligenceHrAdmin\\data\\AssignTaskdata.json",
            page.create_task_maintenance_page
        )



